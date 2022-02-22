from django import forms
from captcha.fields import CaptchaField


from .models import GetInTuch

class contactForm(forms.ModelForm):
    contactName = forms.CharField(min_length=2, max_length=50)
    contactEmail = forms.EmailField(max_length=200)
    contactSubject = forms.CharField(max_length=60)
    contactMessage = forms.CharField(max_length=8000)
    captcha = CaptchaField()
    class Meta:
        model = GetInTuch
        fields = ('contactName','contactEmail','contactSubject','contactMessage','captcha')