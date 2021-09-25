from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Business, NeighbourHood
from .forms import AddBusiness

# Create your views here.
def home(request): 
    neighbourhoods=NeighbourHood.objects.all()
    title='Know your neighborhood'
    return render(request, 'index.html', {'title':title, 'neighbourhoods': neighbourhoods})

def details(request,id): 
    neighbourhoods=NeighbourHood.find_neigborhood(NeighbourHood, id)
    title='Know your neighborhood'
    current_user = request.user
    nbd_id=id
    if request.method == 'POST':
        form = AddBusiness(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            business = form.save(commit=False)
            business.user =current_user
            business.nbd =nbd_id
            business.save()
        return redirect('home')

    else:
        form = AddBusiness()
    business=Business.objects.filter(nbd=id)
    return render(request, 'detail.html', {'title':title, 'neighbourhoods': neighbourhoods, 'form':form, 'business': business})

@login_required(login_url='login')
def addBusiness(request):
    title='Add a business'
    current_user = request.user
    if request.method == 'POST':
        form = AddBusiness(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            business = form.save(commit=False)
            business.user =current_user
            business.save()
        return redirect('details')

    else:
        form = AddBusiness()

    return render(request, 'addBusiness.html', {'title':title,'form':form})

def business_details(request,id): 
    business=Business.objects.filter(id=id)
    title='Let us know your business'
    return render(request, 'business_details.html', {'title':title, 'business': business})
