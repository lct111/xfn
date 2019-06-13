from django import forms
from .models import Pinglun

class PlForm(forms.ModelForm):
    class Meta():
        model = Pinglun
        fields = ['name','email','url','content']
        widgets={
            'content':forms.Textarea()
        }