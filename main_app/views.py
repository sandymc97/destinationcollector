from django.shortcuts import render


# baby step usually a model is used 
destinations = [
  {'location': 'St. Lucia', 'continent': 'North America', 'climate': 'tropical', 'language': 'English'},
  {'location': 'Costa Rica', 'continent': 'North America', 'climate': 'tropical', 'language': 'Spanish'},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def destinations_index(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'destinations/index.html', {
    'destinations': destinations
  })