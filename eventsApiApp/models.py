from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Event(models.Model):
    class StateChoice(models.TextChoices):
        MadhyaPradesh = 'MadhyaPradesh, MP'
        Gujarat = 'Gujarat, Guj'
        UttarPradesh = 'UttarPradesh, UP'
        Karnataka = 'Karnataka, Kar'
    
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=StateChoice.choices, default=StateChoice.MadhyaPradesh)
    zipcode = models.CharField(max_length=10)
    other = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    list_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        verbose_name_plural = 'events'

    def __str__(self):
        return self.title