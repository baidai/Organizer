from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
		task_title = models.CharField(max_length = 200)
		task_summary = models.TextField()
		task_date = models.DateTimeField("Date Added", default=datetime.now())

		def __str__(self):
			return self.task_title