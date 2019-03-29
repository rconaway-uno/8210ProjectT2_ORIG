
from .models import *
from django import forms
from django.contrib.auth.models import User



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_type', 'event_description')
