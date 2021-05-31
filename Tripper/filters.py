from trip.models import Trip
import django_filters


class TripFilter(django_filters.FilterSet):
    class Meta:
        model = Trip
        fields = ( 'category', 'subject', 'activities','start_date','end_date')
