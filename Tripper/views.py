from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.shortcuts import get_object_or_404

from .forms import SignUpForm, ProfileEdit, TripForm

from trip.models import Trip, UserLiking, TripActivities
from users.models import User
from wiki.models import Article


from .filters import TripFilter



def index(request):
    status = Trip.objects.exclude(geo_json__isnull=True)
    return render(request, 'index.html',{'trips':status})

def map(request):
    status = Trip.objects.exclude(geo_json__isnull=True)
    return render(request, 'map.html',{'trips':status})


def trips(request):
    trips = Trip.objects.all().order_by('-created_at')
    return render(request, 'trip.html',{'trips':trips})

def tripDetail(request, id ):
    trip = Trip.objects.get(pk=id)
    if request.user.is_authenticated:
        if UserLiking.objects.filter(user_id=request.user, trip_id=id):
            like = UserLiking.objects.get(user_id=request.user, trip_id=id)
        else:
            like = None
    else: 
        like = None 
    return render(request, 'tripDetail.html',{'trip':trip, 'like': like })

def tripLiking(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if UserLiking.objects.filter(user_id=request.user, trip_id=trip):
        UserLiking.objects.get(user_id=request.user, trip_id=trip).delete()
    else:
        newlike = UserLiking.objects.create(user_id=request.user, trip_id=trip)
    return redirect(request.META['HTTP_REFERER'])


def addTrip(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TripForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_trip = form.save(commit=False)
            new_trip.auther = request.user
            new_trip.save()
            # redirect to a new URL:
            return redirect('../trip')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TripForm()

    return render(request, 'tripAdd.html', {'form': form})



def wiki(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'wiki.html',{'articles':articles})

def articleDetail(request, id ):
    article = Article.objects.get(pk=id)
    return render(request, 'articleDetail.html',{'article':article})



def profile(request):
    user = request.user
    if request.method == 'POST':
        instance = get_object_or_404(User, id=request.user.id)
        form = ProfileEdit(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return render(request, "profile.html", {"user" : user, 'form' : form})
    else:
        form = ProfileEdit()
    return render(request, "profile.html", {"user" : user,'form' : form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def myTrips(request):
    if request.user.is_authenticated:
        trips = Trip.objects.filter(auther = request.user.id)
        context = {'trips': trips }
        return render(request, 'myTrips.html', context)
    else:
        return HttpResponse("not user")

def tripFilterView(request):
    activities = TripActivities.objects.all()
    trips = Trip.objects.all()
    filtered_trip = TripFilter(request.GET, queryset=trips)
    return render(request, 'tripFilter.html', {'filter': filtered_trip, 'activities' : activities})


def myLikes(request):
    if request.user.is_authenticated:
        likes = UserLiking.objects.filter(user_id=request.user).values_list('trip_id', flat=True) 
        trips = Trip.objects.filter(id__in = likes)
        context = {'trips': trips }
        return render(request, 'myLikes.html', context)
    else:
        return HttpResponse("not user")




def search(request):        
   if request.GET.get('search'): # write your form name here      
        name =  request.GET.get('search')      
        try:
            status = Trip.objects.filter(subject__icontains=name)
            return render(request,"search.html",{"trips":status})
        except:
            return render(request,"search.html",{'trips':status})
   else:
        return render(request, 'search.html', {'trips':status})
        
def FAQ(request):
    return render(request, 'FAQ.html')
