from msilib.schema import tables
from unicodedata import name
from django.test import TestCase
from django.contrib.auth.models import User

from project.forms import MeetingForm
from .models import Meeting, Meetingminutes, Resource, Event, Members
from django.urls import reverse_lazy, reverse
import datetime
from .forms import EventForm, MeetingForm


# Create your tests here.

class MeetingTest(TestCase):
     def setUp(self):
          self.type=Meeting(meetingtitle='Meeting')

     def test_typestring(self):
          self.assertEqual(str(self.type), 'Meeting')
     
     def test_tablename(self):
          self.assertEqual(str(Meeting._meta.db_table), 'Meeting')


class ResourceTest(TestCase):
     def setUp(self):
          self.type=Resource(resourcename='Resource')

     def test_typestring(self):
          self.assertEqual(str(self.type), 'Resource')

     def test_tablename(self):
          self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
     def setUp(self):
          self.type=Event(eventtitle='Event')

     def test_typestring(self):
          self.type=Event(str(self.type), 'Event')

     def test_tablename(self):
          self.assertEqual(str(Event._meta.db_table), 'Event')


class MembersTest(TestCase):
     def setUp(self):
          self.type=Members(member='Members')

     def test_typestring(self):
          self.type=Members(str(self.type), 'Members')

     def test_tablename(self):
          self.assertEqual(str(Members._meta.db_table), 'Members')

#Class Meetingminutes isn't working. I think because this has a foreignkey to Meeting.

class MeetingminutesTest(TestCase):
     def setUp(self):
          self.type=Meetingminutes(meetingID='MeetingMinutes')
          
     def test_typestring(self):
          self.type=Meetingminutes(str(self.type), 'Meetingminutes')
          
     def test_tablename(self):
          self.assertEqual(str(Meetingminutes._meta.db_table), 'Meetingminutes')


class newMeetingForm(TestCase):
     def test_meetingform(self):
          data={
               'meetingtitle': 'First Meeting!',
               'meetingdate': 'May 03, 2022',
               'meetinglocation': 'Seattle, WA',
               'meetingagenda': 'To have some fun!',
               }
          form=MeetingForm (data)
          self.assertTrue(form.is_valid)


class newEventForm(TestCase):
     def test_eventform(self):
          data={
               'eventitle': 'Wild Event!',
               'location' : 'Seattle, WA',
               'eventdate': '2022-05-29',
               'eventtime': '12:00:00',
               'eventdescription': 'Huge gathering!',
               'userid': 'Pablo',
          }
          form=EventForm (data)
          self.assertTrue(form.is_valid)
















