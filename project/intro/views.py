from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, DocumentForm
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView
from .forms import TaskForm
from . import forms
from django.shortcuts import get_object_or_404
# Create your views here.

def homepage(request):
	return render(request = request,
		template_name = "intro/home.html",
		context = {"task": Task.objects.all()})  

def new(request):
	form = TaskForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("intro:homepage")
	return render(request = request,
    	template_name = "intro/new.html",
    	context={"form": form})

def list(request, id=None):
	instance = get_object_or_404(Task, id=id)
	form = TaskForm(request.Post or None, request.FILES, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
		}
	return render(request, "list.html", context)



#def new_view(request):
	#preset_form = forms.TaskForm()
#json dumps not yet work
	#return render(request = request,
    	#template_name = "intro/new_task.html",
    	#{'array': json.dumps(data, cls=SpecialEncoder),
		#'preset_form': preset_form,})

class TaskCreate(CreateView):
	model = Task
	fields = ["task_title", "task_category", "task_importance", "task_date", "task_target", "task_acheived", "task_pic","task_summary"]

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

