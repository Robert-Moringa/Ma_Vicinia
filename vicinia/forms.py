from django import forms
from .models import Profile, Business,Police,Post,Health
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','pub_date']

class AddPolice(forms.ModelForm):
    class Meta:
        model = Police
        exclude = ['user','pub_date']

class AddHealth(forms.ModelForm):
    class Meta:
        model = Health
        exclude = ['user','pub_date']

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','pub_date']

class AddProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','pub_date']

# trial
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']