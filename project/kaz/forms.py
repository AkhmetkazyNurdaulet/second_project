from django import forms
from .models import *



class Registration(forms.ModelForm):
    class Meta:
        model = Tourists
        fields = '__all__'




