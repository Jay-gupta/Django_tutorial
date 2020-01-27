from django import forms
from home.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

#form trial
# class ContactForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     gender = forms.ChoiceField(choices = [('male', 'Male'), ('female', 'Female')])

