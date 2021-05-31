from rest_framework import serializers
from .models import *
from users.serializers import UserSummerySerializer
from datetime import date


# class CategorySerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
#     names = serializers.SerializerMethodField()
#     def get_names(self, obj):
#         return TripCategory.TYPE_OF_TRIP_CHOICES
#     class Meta:
#         model = TripCategory


class ActivitieSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = TripActivities
        fields = ['id', 'title']

class TripPostSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = Trip
        fields = '__all__'
        


class TripSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    places = serializers.PrimaryKeyRelatedField(many=True, queryset = Place.objects.all())
    auther = UserSummerySerializer()
    trip_days = serializers.SerializerMethodField('get_days')
    
    class Meta:
        model = Trip
        fields = [
            'id' ,
            'subject',
            'category',
            'description',
            'activities',
            'auther',
            'image',
            'category',
            'places',
            'trip_days',
            'geo_json',
            'created_at',
            'start_date',
            'end_date',
            ]
        
    @staticmethod
    def get_days(obj):
        if obj.end_date and obj.start_date : 
            delta = obj.end_date - obj.start_date
            return  delta.days
        else :
            return None


class TripSummerySerializer(serializers.ModelSerializer): 
    places = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    auther = UserSummerySerializer()
    trip_days = serializers.SerializerMethodField('get_days')
    # category = CategorySerializer()

    class Meta:
        model = Trip
        fields = [
            'id' ,
            'subject',
            'category',
            'description',
            'activities',
            'auther',
            'image',
            'category',
            'places',
            'trip_days',
            ]
        read_only_fields = fields

    @staticmethod
    def get_days(obj):
        if obj.end_date and obj.start_date : 
            delta = obj.end_date - obj.start_date
            return  delta.days
        else :
            return None

class PlaceSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = Place
        fields = '__all__'
        
        
class LikingSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = UserLiking
        fields = '__all__'
        
