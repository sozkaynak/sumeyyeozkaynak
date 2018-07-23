from django import forms
from .models import Post,PostComment
from captcha.fields import ReCaptchaField

#Post Yayınlama Sistemi 1.0

#Post Yorum Sistemi 2.0 --> 3.0 için blog:views.py sayfasına gidiniz.
class PostCommentForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model=PostComment
        fields=[
            'name',
            'content'
        ]