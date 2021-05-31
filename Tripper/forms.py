from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from trip.models import Trip, TripActivities

from django.forms import ModelForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


class ProfileEdit(ModelForm):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email', 'about', 'avatar' )
        
    def __init__(self, *args, **kwargs):
        super(ProfileEdit, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['about'].widget.attrs.update({'class' : 'form-control mt-2'})
        

        

class TripForm(ModelForm):
    activities = forms.ModelMultipleChoiceField(TripActivities.objects.all())
    class Meta:
        model = Trip
        fields = ( 'category', 'subject', 'description', 'activities','start_date','end_date','image','geo_json' )

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class' : 'form-select mt-2'})
        self.fields['subject'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['activities'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['start_date'].widget.attrs.update({'class' : 'form-control mt-2', 'type': 'date'})
        self.fields['end_date'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['image'].widget.attrs.update({'class' : 'form-control mt-2'})
        self.fields['geo_json'].widget.attrs.update({'class' : 'form-control mt-2'})



