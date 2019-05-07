from django.contrib import admin
from .models import Task 
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		("title/date", {"fields":["task_title", "task_date"]}),
		("content", {"fields":["task_summary"]})
		]

	formfield_overrides= {
		models.TextField:{'widget': TinyMCE()}
		}
admin.site.register(Task, TaskAdmin)