from django import forms
from .models import Meeting, Event, Members


class MeetingForm(forms.ModelForm):
     class Meta:
          model=Meeting
          fields='__all__'

class EventForm(forms.ModelForm):
     class Meta:
          model=Event
          fields='__all__'
