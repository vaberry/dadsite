from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View, TemplateView
from .models import StoryModel
import os

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")


class Home(TemplateView):
    template_name='home.html'

class Gallery(View):
	def get(self, request):
		print('REQUEST IS GETTTT')
		if request.method == "GET":
			# family_images_list = os.listdir('/home/vberry/django-projects/dadsite/dadsite/main/static/img/family_man')
			# athlete_images_list = os.listdir('/home/vberry/django-projects/dadsite/dadsite/main/static/img/athlete')
			# badass_images_list = os.listdir('/home/vberry/django-projects/dadsite/dadsite/main/static/img/badass')

	
			# context = {
			# 	'images' : 
			# 	'family' : family_images_list,
			# 	'athlete' : athlete_images_list,
			# 	'badass' : badass_images_list,
			# }
			return render(request, 'gallery.html')
	
class Story(View):
	def get(self, request):
		if request.method == "GET":
			if 'user_story' in request.GET:
				name = request.GET.get("name")
				if name == '':
					name = 'Friend of Vince'
				msg = request.GET.get("msg")
				relationship = request.GET.get("relationship")

				StoryModel.objects.create(
					name = name,
					body = msg,
					relationship = relationship,
				)

				return redirect('story')
		
			context = {
				'stories' : StoryModel.objects.all().order_by('-created_on')
			}
			return render(request, 'story.html', context=context)

class Arrangements(TemplateView):
	template_name='arrangements.html'
