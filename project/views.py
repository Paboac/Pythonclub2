from multiprocessing import context
from turtle import title
from urllib import request
from django.shortcuts import render, get_object_or_404
from project.forms import MeetingForm
from .models import Meetingminutes, Resource, Event, Meeting, Members
from django.urls import reverse_lazy
from .forms import EventForm, MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
     return render(request, 'project/index.html')

def resource(request):
     resource_list=Resource.objects.all() 
     return render(request, 'project/resource.html', {'resource_list': resource_list})

def meeting(request):
     meeting_list=Meeting.objects.all()
     return render(request, 'project/meeting.html', {'meeting_list': meeting_list})

def event(request):
     even_title=Event.objects.all()
     return render(request, 'event.html', {'even_title': even_title})


def meetingDetails(request, id):
     meeting=get_object_or_404(Meeting, pk=id)
     minute=Meetingminutes.objects.get(meetingID=meeting.id)
     context={
          'meeting' : meeting,
          'minute' : minute,
     }
     return render(request, 'project/meetingDetails.html', {'meeting': meeting, 'minute': minute})

def eventDetails(request, id):
     event=get_object_or_404(Event, pk=id)
     title=Event.objects.get(eventitle=event.id)
     return render(request, 'project/eventDetails.html', {'event':event, 'title':title})
     
@login_required
def newMeeting(request):
     form=MeetingForm

     if request.method=='POST':
          form= MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save
               form=MeetingForm()

     else:
          form=MeetingForm
     return render(request, 'project/newmeeting.html', {'form': form})


def newEvent(request):
     form=EventForm
     if request.method=='POST':
          form= EventForm(request.post)
          if form.is_valid():
               post=form.save(commit=True)
               post.save
               form=EventForm()
     else:
          form=EventForm
          return render(request, 'project/newevent.html', {'form':form})


def loginmessage(request):
     return render(request, 'project/loginmessage.html')
def logoutmessage(request):
     return render(request, 'project/logoutmessage.html')











     
     


