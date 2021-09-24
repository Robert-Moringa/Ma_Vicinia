from django.shortcuts import render
from .models import NeighbourHood

# Create your views here.
def home(request): 
    neighbourhoods=NeighbourHood.objects.all()
    title='Know your neighborhood'
    return render(request, 'index.html', {'title':title, 'neighbourhoods': neighbourhoods})

def details(request,id): 
    neighbourhoods=NeighbourHood.find_neigborhood(NeighbourHood, id)
    title='Know your neighborhood'
    return render(request, 'detail.html', {'title':title, 'neighbourhoods': neighbourhoods})