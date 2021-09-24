from django.shortcuts import render
from .models import NeighbourHood

# Create your views here.
def home(request): 
    neighbourhoods=NeighbourHood.objects.all()
    title='Know your neighborhood'
    return render(request, 'home.html', {'title':title, 'neighbourhoods': neighbourhoods})