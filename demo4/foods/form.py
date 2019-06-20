from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy

class MyUserLogin(forms.ModelForm):

    class Meta():
        model=MyUser
        fields=['username','password']
        widgets = {"password": forms.PasswordInput(attrs={"class": "form-control",'placeholder':'密码'}),
                   "username": forms.TextInput(attrs={"class": "form-control",'placeholder':'账号'})
                   }

        help_texts = {
            "username": gettext_lazy(""),
        }


class MyUserRegist(forms.ModelForm):

    class Meta():
        model=MyUser
        fields=['username','email','password']
        widgets = {"password": forms.PasswordInput(attrs={"class": "form-control",'placeholder':'密码'}),
                   "username": forms.TextInput(attrs={"class": "form-control",'placeholder':'账号'}),
                   "email": forms.EmailInput(attrs={"class": "form-control",'placeholder':'邮箱'})
                   }
        help_texts = {
            "username": gettext_lazy(""),
        }