from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class CreateQModel(models.Model):
    task_name = models.CharField(max_length=100)
    fruit_CHOICES = (('Apple', 'Apple'), ('Banana', 'Banana'), ('Mango', 'Mango'), ('Grape', 'Grape'))
    fruit = models.CharField(max_length=100, choices=fruit_CHOICES)
    quantity = models.IntegerField()
    repeats = models.IntegerField()

    shcedule_CHOICES = (
        ('Once', 'Once'), 
        ('Minutes', 'Minutes'), 
        ('Hourly', 'Hourly'), 
        ('Daily', 'Daily'), 
        ('Weekly', 'Weekly'), 
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly'),
        ('Cron', 'Cron')
        )
    schedule_type = models.CharField(max_length=100, choices=shcedule_CHOICES)
    schedule_quantity = models.IntegerField(default=-1)
    start_time = models.DateTimeField()


class CreateTaskModel(models.Model):
    fruit_CHOICES = (('Apple', 'Apple'), ('Banana', 'Banana'), ('Mango', 'Mango'), ('Grape', 'Grape'))
    fruit = models.CharField(max_length=100, choices=fruit_CHOICES)
    quantity = models.IntegerField()
    create_time = models.DateTimeField(default=timezone.now)