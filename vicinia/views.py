from django.shortcuts import render

# Create your views here.
def home(request): 
    title='Know your neighborhood'
    return render(request, 'home.html', {'title':title,})