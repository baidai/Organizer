from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.

def homepage(request):
	return render(request = request,
		template_name = "intro/home.html",
		context = {"task": Task.objects.all()})  

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created:{username}")
			login(request, user)
			return redirect("intro:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
			
			return render(request = request,
				template_name = "intro/register.html",
				context={"form":form})
				
	form = NewUserForm
	return render(request,
					"intro/register.html",
					context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully. Comeback soon!")
	return redirect("intro:homepage")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "Welcome Back:{username}!")
				return redirect('/')
			else:
				messages.error(request, "Seems something wasn't right, please try again.")

		else:
			messages.error(request, "Oops... Try again. Something wasn't right.")

	form = AuthenticationForm()
	return render(request = request,
				template_name = "intro/login.html",
				context={"form":form})

def upload(request):
	context = {}
	if request.method == "POST":
		upload_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(upload_file.name, upload_file)
		context['url'] = fs.url(name)
		return render(request,'intro/pic.html', context)
	return render(request,'intro/pic.html')
