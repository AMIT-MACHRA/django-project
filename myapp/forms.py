from django import forms
from myapp.models import *


class loginform(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"




class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"