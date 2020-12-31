from rest_framework import serializers
from .models import *
from users.serializers import UserSummerySerializer
from datetime import date


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TripImage
#         exclude = ['exif']


class CategorySerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = TripCategory
        fields = '__all__'
    

class TripSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    places = serializers.PrimaryKeyRelatedField(many=True, queryset = Place.objects.all())
    
    class Meta:
        model = Trip
        fields = '__all__' 

class TripSummerySerializer(serializers.ModelSerializer): 
    places = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    autherdetail = UserSummerySerializer()
    trip_days = serializers.SerializerMethodField('get_days')
    category = CategorySerializer()

    class Meta:
        model = Trip
        fields = [
            'id' ,
            'subject',
            'category',
            'description',
            'activities',
            'auther',
            'autherdetail',
            'image',
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
