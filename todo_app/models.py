import datetime

import self as self
from django.db import models


# Create your models here.
from django.db.models import CharField


class Task(models.Model):
    def __str__(self):
        return self.name
    name: CharField = models.CharField(max_length=100)
    priority = models.IntegerField()
    date=models.DateField(default=datetime.date.today)
