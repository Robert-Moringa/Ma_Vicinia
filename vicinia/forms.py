from django import forms
from .models import Profile, Business,Police,Post,Health

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