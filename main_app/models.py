from django.db import models
from django.urls import reverse

# Create your models here.


class Destination(models.Model):
    location = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.location} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'destination_id': self.id})
