from django import forms
from .models import Article, ArticleComment,SubjectComment,CategoryComment
from captcha.fields import ReCaptchaField

#Article Yayınlama Sistemi 1.0


#Category Yorum Sistemi 2.0 --> 3.0 için myworkandresearch:views.py sayfasına git
class CategoryCommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = CategoryComment
        fields = [
            'name',
            'content'
        ]

#Subject Yorum Sistemi 2.0 --> 3.0 için myworkandresearch:views.py sayfasına git
class SubjectCommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = SubjectComment
        fields = [
            'name',
            'content'
        ]

#Article Yorum Sistemi 2.0 --> 3.0 için myworkandresearch:views.py sayfasına git
class ArticleCommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ArticleComment
        fields = [
            'name',
            'content'
        ]