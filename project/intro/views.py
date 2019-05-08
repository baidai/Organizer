from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def homepage(request):
	return render(request = request,
		template_name = "intro/home.html",
		context = {"task": Task.objects.all()})  

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("intro:homepage")
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
				
	form = UserCreationForm
	return render(request,
					"intro/register.html",
					context={"form":form})