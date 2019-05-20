from django.db import models
from datetime import datetime
from django.utils import timezone
from django import forms
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models

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
        #task_summary = models.TextField("Summary")
        task_summary = tinymce_models.HTMLField(null=True, blank=True)
        task_date = models.DateField("Added or Updated", default=timezone.now())
        task_target = models.DateField("Target Date", null=True, blank=True)
        task_acheived = models.DateField("Date Acheived", null=True, blank=True)
        task_pic = models.FileField("Image", null= True, blank=True)

        #defines a human readable representation of a model
        def __str__(self):
            return self.task_title

        #set url link to model
        def get_absolute_url(self):
            return reverse("intro:homepage", kwargs={"id": self.id})




			