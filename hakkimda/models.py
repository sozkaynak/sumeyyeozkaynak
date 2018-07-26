from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Hakkimda(models.Model):
    name=models.CharField(max_length=200)
    text=RichTextField()
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

