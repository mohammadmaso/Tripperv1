"""Tripper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from users import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from users.views import UserViewSet, FollowerViewSet, FollowingViewSet, UserSummeryViewSet
from trip.views import TripViewSet, PlaceViewSet, TripSummeryViewSet, LikeViewSet, TripPostViewSet
from wiki.views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from . import views


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'followers', FollowerViewSet, basename='follower')
router.register(r'following', FollowingViewSet, basename='following')
router.register(r'trip', TripViewSet, basename='trip')
router.register(r'tripPost', TripPostViewSet, basename='tripPost')
router.register(r'tripSummery', TripSummeryViewSet, basename='tripSummery')
router.register(r'place', PlaceViewSet, basename='place')
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'likes', LikeViewSet, basename='likes')



#router.register(r'userSummery', UserSummeryViewSet, basename='userSummery')



# Admin site configurations 
admin.site.site_header = "Tripper Admin Panel"
admin.site.site_title = "Tripper Admin Panel"
admin.site.index_title = "Welcome to Tripper Admin Panel"



urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.loginView, name='login1'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('trip/', views.trips, name='trip'),
    url(r'tripDetail/like/(?P<trip_id>\d+)', views.tripLiking, name='tripLiking'),
    url(r'^tripDetail/(?P<id>\d+)', views.tripDetail, name='tripDetail'),
    path('wiki/', views.wiki, name='wiki'),
    url(r'^articleDetail/(?P<id>\d+)', views.articleDetail, name='articleDetail'),
    path('profile/', views.profile, name='profile'),
    path('myTrips/', views.myTrips , name = 'myTrips'),
    path('myLikes/', views.myLikes, name='myLikes'),
    url(r'^tripFilter/$', views.tripFilterView, name='tripFilter'),
    url(r'^search/$', views.search, name='search'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('addTrip/', views.addTrip, name='addTrip'),









    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


