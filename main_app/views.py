from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Destination
from .forms import WeatherForm




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
  weather_form = WeatherForm()
  return render(request, 'destinations/detail.html', {
    'destination': destination, 'weather_form': weather_form
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

def add_weather(request, destination_id):
  # create a ModelForm instance using the data in request.POST
  form = WeatherForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_weather = form.save(commit=False)
    new_weather.destination_id = destination_id
    new_weather.save()
  return redirect('detail', destination_id=destination_id)