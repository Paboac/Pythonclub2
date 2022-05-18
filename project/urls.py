from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('resource/', views.resource, name='resource'),
     path('meeting/', views.meeting, name='meeting'),
     path('event/', views.event, name='event'),
     path('meetingDetails/<int:id>', views.meetingDetails, name ='detail'),
     path('newMeeting/', views.newMeeting, name='newmeeting'),
     path('newevent/', views.newEvent, name='newevent'),
     path('eventDetails/<int:id>', views.eventDetails, name='events'),
     path('loginmessage/', views.loginmessage, name='loginmessage'),
     path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]