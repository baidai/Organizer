from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Task(models.Model):
        level_of_importance = (
        ('N', 'NA'),
        ('T', 'To do'),
        ('I', 'Important'),
        ('U', 'Urgent'),
        )
        task_importance = models.CharField(
        "Level of Importance",
        max_length=1,
        choices=level_of_importance,
        default='N',
        )
        Category = (
        ('D', 'Daily Task'),
        ('C', 'Career'),
        ('E', 'Educational'),
        ('F', 'Financial'),
        ('H', 'Health'),
        ('M', 'Family Members'),
        ('P', 'Personal'),   
        ('R', 'Relationship'),
        ('S', 'Spiritual'),    
        )
        task_category = models.CharField(
        "Category",
        max_length=1,
        choices=Category,
        default='D',
        )
        task_title = models.CharField("Title", max_length = 200)
        task_summary = models.TextField("Summary")
        task_date = models.DateField("Added or Updated", default=timezone.now())
        task_target = models.DateField("Target Date", null=True, blank=True)
        task_acheived = models.DateField("Date Acheived", null=True, blank=True)
        task_pic = models.FileField("Image", upload_to="task/media/", null= True, blank=True)

        def __str__(self):
            return self.task_title



			