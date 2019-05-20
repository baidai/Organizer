from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task
from tinymce.widgets import TinyMCE
from django.views.generic.edit import CreateView
from django.forms import ModelForm
from . import models

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user	


class TaskForm(forms.ModelForm):
    class Meta:
    	model = Task
    	fields = ("task_title", "task_category", "task_importance", "task_date", "task_target", "task_acheived", "task_pic","task_summary")

class DocumentForm(CreateView):
	model = Task 

#using widget for html https://docs.djangoproject.com/en/2.2/ref/forms/widgets/
