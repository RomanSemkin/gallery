from django.conf import settings
from django.core.mail import BadHeaderError
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, FormView

from .forms import ContactForm
from .models import Pictures, Images
from .tasks import send_email_celery


class AboutView(TemplateView):
    template_name = "pictures/about.html"


class ContactView(FormView):
    template_name = 'pictures/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        subject = 'FROM_GALLERY'
        name = form.cleaned_data.get('name')
        sender = form.cleaned_data.get('sender')
        message = "{name} / {email} said: ".format(
            name=name,
            email=sender)
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        recipients = [settings.ADMIN_EMAIL]
        if message and sender:
            try:
                send_email_celery.delay(subject, sender, message, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return super(ContactView, self).form_valid(form)


class PicturesListView(ListView):
    model = Pictures
    template_name = "pictures/list.html"
    paginate_by = 9
    queryset = Pictures.objects.filter(active=True).all()


class PicturesDetailSlugView(DetailView):
    queryset = Pictures.objects.all()
    template_name = "pictures/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Pictures.objects.get(slug=slug, active=True)
        except Pictures.DoesNotExist:
            raise Http404("Not found..")
        except Pictures.MultipleObjectsReturned:
            qs = Pictures.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            images = Images.objects.get(picture=self.object)
        except Images.DoesNotExist:
            # raise Http404("Not found..")
            return context
        context['images'] = images
        return context
