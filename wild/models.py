from django.db import models

# Create your models here.

class Event(models.Model):
     banner = models.ImageField()
     event = models.CharField(max_length=40)
     venue = models.CharField(max_length=40)
     contacts = models.IntegerField()
     date = models.DateField()
     time = models.TimeField(max_length=40)
     cash = models.CharField(max_length=40)

     def __str__(self):
         return self.event

class Comment(models.Model):
     event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
     user_name = models.CharField(max_length=40)

     def __str__(self):
         return self.user_name
