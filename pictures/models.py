import random
import os

from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "pictures/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class Pictures(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True, default='slug')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pictures:detail", kwargs={"slug": self.slug})


def pre_save_receiver_page_model(sender, instance, *args, **kwargs):
    if instance.slug == 'slug' or instance.slug == '':
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver_page_model, sender=Pictures)