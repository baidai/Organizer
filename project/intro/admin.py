from django.contrib import admin
from .models import Task 
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	fieldsets = [
		("title/date", {"fields":["task_title", "task_category", "task_importance", "task_date", "task_target", "task_acheived"]}),
		("content", {"fields":["task_pic", "task_summary"]})
		]

	formfield_overrides= {
		models.TextField:{'widget': TinyMCE()}
		}
		
admin.site.register(Task, TaskAdmin)