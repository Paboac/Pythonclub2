from urllib import request
from django.shortcuts import render
from .models import Resource, Event, Meeting, Members


# Create your views here.
def index(request): 
     return render(request, 'project/index.html')

def resource(request):
     resource_list=Resource.objects.all() 
     return render(request, 'project/resource.html', {'resource_list': resource_list})

