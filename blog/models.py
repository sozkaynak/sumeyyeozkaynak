from django.db import models
from django.utils import timezone
from django.urls import reverse


    # Modeller arasında sadece OneToOne ilişkisi kurulmuştur.
       # There is only one One To Onerelationship between the models.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategori Adı')
    statement = models.TextField(max_length=200, verbose_name='Kategori Açıklaması')
    text=models.TextField(verbose_name='Kategori Metni')
    slug = models.SlugField(max_length=200, verbose_name='Kategori Url')

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='Konu Adı')
    statement = models.TextField(max_length=100, verbose_name='Konu Açıklaması')
    text = models.TextField(verbose_name='Konu Metni')
    slug = models.SlugField(max_length=200, verbose_name='Konu Url')

    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Kategori Adı')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:subject', args=[self.slug, self.category_name.slug])

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=200, verbose_name='Başlık')
    slug = models.SlugField(max_length=200, verbose_name='Yazı Url')
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    subject_name = models.ForeignKey('Subject', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('nlog:detail', args=[self.slug, self.subject_name.slug, self.subject_name.category_name.slug])