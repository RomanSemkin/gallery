from django.conf.urls import url

from .views import PicturesListView, PicturesDetailSlugView, AboutView, ContactView

app_name = 'pictures'
urlpatterns = [
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
    url(r'^(?P<slug>[\w-]+)/$', PicturesDetailSlugView.as_view(), name='detail'),
    url(r'^$', PicturesListView.as_view(), name='list'),
]