from django.db import models
from django.utils import timezone
from django.urls import reverse


    # Modeller arasında sadece OneToOne ilişkisi kurulmuştur.
       # There is only one One To Onerelationship between the models.

class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategori Adı')
    slug = models.SlugField(max_length=200, verbose_name='Kategori Url')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar', related_name='+')
    title = models.CharField(max_length=200, verbose_name='Başlık')
    slug = models.SlugField(max_length=200, verbose_name='Yazı Url')
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    topic_name = models.ForeignKey('Topic', on_delete=models.CASCADE,  default='SOME STRING')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug, self.topic_name.slug])