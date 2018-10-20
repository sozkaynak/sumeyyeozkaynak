from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


    # Modeller arasında sadece OneToOne ilişkisi kurulmuştur.
       # There is only one One To Onerelationship between the models.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategori Adı')
    slug = models.SlugField(unique=True, max_length=210, verbose_name='Kategori Url', editable=False)
    text = RichTextField(verbose_name='Kategori Metni')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myworkandresearch:category',
                       args=[self.slug, self.subject_name.slug, self.subject_name.category_name.slug])

    def get_unique_slug(self):
        slug=slugify(self.name.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Category.objects.filter(slug=unique_slug).exists(): #böyle bir slug var mı ? yok mu ?
            unique_slug= '{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']
# Category Yorum Sistemi 1.0 --> 2.0 için forms.py sayfasına git
class CategoryComment(models.Model):
    category = models.ForeignKey('myworkandresearch.Category', related_name='categorys',
                                on_delete=models.CASCADE)  # on_delete=models.CASCADE ile bir Post siindiğinde onunla alakalı tüm yorumlarda silinmiş oluyor.

    name = models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)  # True diyerek tarih bilgisini otomatik dolduruyo


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='Konu Adı')
    slug = models.SlugField(unique=True, max_length=210, verbose_name='Konu Url', editable=False)
    text = RichTextField(verbose_name='Konu Metni')

    
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Kategori Adı')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myworkandresearch:subject', args=[self.slug, self.category_name.slug])

    def get_unique_slug(self):
        slug=slugify(self.name.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Subject.objects.filter(slug=unique_slug).exists(): #böyle bir slug var mı ? yok mu ?
            unique_slug= '{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug


    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Subject, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']
# Subject Yorum Sistemi 1.0 --> 2.0 için forms.py sayfasına git
class SubjectComment(models.Model):
    subject = models.ForeignKey('myworkandresearch.Subject', related_name='subjects',
                                on_delete=models.CASCADE)  # on_delete=models.CASCADE ile bir Post siindiğinde onunla alakalı tüm yorumlarda silinmiş oluyor.

    name = models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)  # True diyerek tarih bilgisini otomatik dolduruyo


class Article(models.Model):

    user=models.ForeignKey('auth.User', verbose_name='Yazar', related_name='articles',on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Başlık')
    slug = models.SlugField(unique=True,max_length=210, verbose_name='Yazı Url', editable=False)
    text = RichTextField()
    image = models.ImageField(null=True, blank=True)
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
         return reverse('myworkandresearch:detail', args=[self.slug, self.subject_name.slug, self.subject_name.category_name.slug])

    def get_unique_slug(self):
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Article.objects.filter(slug=unique_slug).exists(): #böyle bir slug var mı ? yok mu ?
            unique_slug= '{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-published_date', '-id']
# Article Yorum Sistemi 1.0 --> 2.0 için forms.py sayfasına git
class ArticleComment(models.Model):

    article= models.ForeignKey('myworkandresearch.Article', related_name='comments', on_delete=models.CASCADE)#on_delete=models.CASCADE ile bir Post siindiğinde onunla alakalı tüm yorumlarda silinmiş oluyor.

    name=models.CharField(max_length=200, verbose_name='İsim')
    content=models.TextField(verbose_name='Yorum')

    created_date=models.DateTimeField(auto_now_add=True) #True diyerek tarih bilgisini otomatik dolduruyo