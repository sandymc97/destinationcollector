from django.contrib import admin
from .models import Destination, Weather

# Register your models here.
admin.site.register(Destination)
admin.site.register(Weather)