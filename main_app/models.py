from django.db import models
from django.urls import reverse
from datetime import date


STATUSES = (
    ('S', 'Sunny'),
    ('R', 'Rainy'),
    ('C', 'Cloudy')
)

class Activity(models.Model):
  name = models.CharField(max_length=50)
 

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('activities_detail', kwargs={'pk': self.id})


class Destination(models.Model):
    location = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return f'{self.location} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'destination_id': self.id})

class Weather(models.Model):
  date = models.DateField()
  status = models.CharField(
    max_length=1,
	 choices=STATUSES,
	 default=STATUSES[0][0]
  )
  
  destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_status_display()} on {self.date}"
    class Meta:
      ordering = ['-date']

