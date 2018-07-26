from django import forms
from .models import Hakkimda, HakkimdaComment
from captcha.fields import ReCaptchaField




#Hakkimda Yorum Sistemi 2.0 --> 3.0 için myworkandresearch:views.py sayfasına git
class HakkimdaCommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Hakkimda
        fields = [
            'name',
            'content'
        ]