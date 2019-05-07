from django.shortcuts import render
from .models import Task


# Create your views here.

def homepage(request):
	return render(request = request,
		template_name = "intro/home.html",
		context = {"task": Task.objects.all()})  
