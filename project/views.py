from multiprocessing import context
from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Meetingminutes, Resource, Event, Meeting, Members
from django.urls import reverse_lazy


# Create your views here.
def index(request): 
     return render(request, 'project/index.html')

def resource(request):
     resource_list=Resource.objects.all() 
     return render(request, 'project/resource.html', {'resource_list': resource_list})

def meeting(request):
     meeting_list=Meeting.objects.all()
     return render(request, 'project/meeting.html', {'meeting_list': meeting_list})

def meetingDetails(request, id):
     meeting=get_object_or_404(Meeting, pk=id)
     minute=Meetingminutes.objects.get(meetingID=meeting.id)
     context={
          'meeting' : meeting,
          'minute' : minute,
     }
     return render(request, 'project/meetingDetails.html', {'meeting': meeting, 'minute': minute})
     
     


