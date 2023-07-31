from django.contrib import admin
from .models import Destination, Weather, Activity

# Register your models here.
admin.site.register(Destination)
admin.site.register(Weather)
admin.site.register(Activity)