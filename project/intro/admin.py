from django.contrib import admin
from .models import Task 
from django.db import models
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		("title/date", {"fields":["task_title", "task_date"]}),
		("content", {"fields":["task_summary"]})
		]

admin.site.register(Task, TaskAdmin)