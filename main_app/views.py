import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Destination, Activity, Photo
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
  id_list = destination.activities.all().values_list('id')
  # Now we can query for activities whose ids are not in the list using exclude
  activities_destination_doesnt_have = Activity.objects.exclude(id__in=id_list)
  weather_form = WeatherForm()
  return render(request, 'destinations/detail.html', {
    'destination': destination, 'weather_form': weather_form,
    'activities': activities_destination_doesnt_have
  })

class DestinationCreate(CreateView):
  model = Destination
  fields = ['location','continent', 'climate', 'language']
 
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
    # has the destination_id assigned
    new_weather = form.save(commit=False)
    new_weather.destination_id = destination_id
    new_weather.save()
  return redirect('detail', destination_id=destination_id)

class ActivityList(ListView):
  model = Activity

class ActivityDetail(DetailView):
  model = Activity

class ActivityCreate(CreateView):
  model = Activity
  fields = '__all__'

class ActivityUpdate(UpdateView):
  model = Activity
  fields = ['name']

class ActivityDelete(DeleteView):
  model = Activity
  success_url = '/activities'

def assoc_activity(request, destination_id, activity_id):
  # Note that you can pass a activity's id instead of the whole activity object
  Destination.objects.get(id=destination_id).activities.add(activity_id)
  return redirect('detail', destination_id=destination_id)

def unassoc_activity(request, destination_id, activity_id):
  # Note that you can pass a activity's id instead of the whole activity object
  Destination.objects.get(id=destination_id).activities.remove(activity_id)
  return redirect('detail', destination_id=destination_id)

def add_photo(request, destination_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to destination_id or destination (if you have a destination object)
            Photo.objects.create(url=url, destination_id=destination_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', destination_id=destination_id)

