from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Business, NeighbourHood,Health,Police
from .forms import AddBusiness, AddPolice, AddHealth

# Create your views here.
def home(request): 
    neighbourhoods=NeighbourHood.objects.all()
    title='Know your neighborhood'
    return render(request, 'index.html', {'title':title, 'neighbourhoods': neighbourhoods})

def details(request,id): 
    neighbourhoods=NeighbourHood.objects.filter(id=id)
    health=Health.objects.filter(nbd=id)
    police=Police.objects.filter(nbd=id)
    title='Know your neighborhood'
    business=Business.objects.filter(nbd=id)
    return render(request, 'detail.html', {'title':title, 'neighbourhoods': neighbourhoods, 'business': business, 'police': police, 'health':health})

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

@login_required(login_url='login')
def business_details(request,id): 
    business=Business.objects.filter(id=id)
    title='Let us know your business'
    return render(request, 'business_details.html', {'title':title, 'business': business})

@login_required(login_url='login')
def addPolice(request):
    title='Security is very paramount'
    current_user = request.user
    if request.method == 'POST':
        form = AddPolice(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            police = form.save(commit=False)
            police.user =current_user
            police.save()
        return redirect('home')

    else:
        form = AddPolice()

    return render(request, 'addPolice.html', {'title':title,'form':form})

@login_required(login_url='login')
def addHealth(request):
    title='Health care for all and sundry'
    current_user = request.user
    if request.method == 'POST':
        form = AddHealth(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            health = form.save(commit=False)
            health.user =current_user
            health.save()
        return redirect('home')

    else:
        form = AddHealth()

    return render(request, 'addHealth.html', {'title':title,'form':form})
