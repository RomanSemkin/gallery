from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Pictures, Images


class AboutView(TemplateView):
    template_name = "pictures/about.html"


class ContactView(TemplateView):
    template_name = "pictures/contact.html"


class PicturesListView(ListView):
    model = Pictures
    template_name = "pictures/list.html"
    paginate_by = 9
    queryset = Pictures.objects.filter(active=True).all()
    # def get_queryset(self, *args, **kwargs):
    #     return Pictures.objects.filter(active=True).all()


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