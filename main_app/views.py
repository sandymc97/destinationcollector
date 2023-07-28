from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Destination




def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def destinations_index(request):
  destinations = Destination.objects.all()
  return render(request, 'destinations/index.html', {
    'destinations': destinations
  })

def destinations_detail(request, destination_id):
  destination = Destination.objects.get(id=destination_id)
  return render(request, 'destinations/detail.html', {
    'destination': destination
  })

class DestinationCreate(CreateView):
  model = Destination
  fields = '__all__'
 
class DestinationUpdate(UpdateView):
  model = Destination
  fields = ['location','continent', 'climate', 'language']

class DestinationDelete(DeleteView):
  model = Destination
  success_url = '/destinations'