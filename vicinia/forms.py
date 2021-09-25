from django import forms
from .models import Profile, Business,Police,Post

class AddBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','pub_date']

