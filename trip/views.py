from django.shortcuts import get_object_or_404
from .serializers import TripSerializer, PlaceSerializer, TripSummerySerializer, LikingSerializer, TripPostSerializer
from .models import Trip, Place, TripImage, UserLiking
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,request


class TripPostViewSet(viewsets.ModelViewSet):
    serializer_class = TripPostSerializer
    queryset = Trip.objects.all()


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

class TripSummeryViewSet(viewsets.ModelViewSet):
    serializer_class = TripSummerySerializer
    queryset = Trip.objects.all().order_by('-created_at')
    ordering = ['create_date']
        
    def get_queryset(self):
        queryset = Trip.objects.all().order_by('-created_at')
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(auther=user)
        return queryset
    


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    
class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikingSerializer
    queryset = UserLiking.objects.all()
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = UserLiking.objects.all()
        user = self.request.query_params.get('user', None)
        trip = self.request.query_params.get('trip', None)

        if user is not None and trip is not None:
            queryset = queryset.filter(user_id=user)
            queryset = queryset.filter(trip_id=trip)
        
        return queryset

