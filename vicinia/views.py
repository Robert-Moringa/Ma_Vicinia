from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Business, NeighbourHood,Health,Police, Post, Profile
from .forms import AddBusiness, AddPolice, AddHealth,AddPost, AddProfile

# Create your views here.
def home(request): 
    neighbourhoods=NeighbourHood.objects.all()
    title='Know your neighborhood'
    return render(request, 'index.html', {'title':title, 'neighbourhoods': neighbourhoods})
    
@login_required(login_url='login')
def details(request,id): 
    neighbourhoods=NeighbourHood.objects.filter(id=id)
    health=Health.objects.filter(nbd=id)
    police=Police.objects.filter(nbd=id)
    posts=Post.objects.filter(nbd=id)
    title='Know your neighborhood'
    business=Business.objects.filter(nbd=id)
    return render(request, 'detail.html', {'title':title, 'posts':posts, 'neighbourhoods': neighbourhoods, 'business': business, 'police': police, 'health':health})

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

@login_required(login_url='login')
def addPost(request):
    title='Post your concerns for your neigbourhood to see'
    current_user = request.user
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            post = form.save(commit=False)
            post.user =current_user
            post.save()
        return redirect('home')

    else:
        form = AddPost()

    return render(request, 'addPost.html', {'title':title,'form':form})

@login_required(login_url='login')
def addProfile(request):
    title='Make your own profile'
    current_user = request.user
    if request.method == 'POST':
        form = AddProfile(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            post = form.save(commit=False)
            post.user =current_user
            post.save()
        return redirect('home')

    else:
        form = AddProfile()
    profile=Profile.objects.filter(user=current_user)
    return render(request, 'addProfile.html', {'title':title,'form':form, 'profile': profile})

@login_required(login_url='login')
def search_business(request,id):
    title="Find"
    
    if 'business_name' in request.GET and request.GET['business_name']:
        search_term = request.GET.get('business_name')
        found_results = Business.objects.filter(nbd=id).filter(name__icontains=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{'title':title,'results': found_results, 'message': message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})