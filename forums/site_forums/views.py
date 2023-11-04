from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, CreatePost, LoginForm, CommentForm
from .models import LoginUser, Comment, Post

def home(request):
	if request.user.is_authenticated:
		posts = Post.objects.all()
		return render(request, 'home.html', {'posts':posts})
	else:
		return redirect('login')
	
def login_user(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Logged In! Welcome!")
			return redirect('home')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'login':form})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def user_post(request, pk):
	if request.user.is_authenticated:
		user_post = Post.objects.get(id=pk)
		return render(request, 'post.html', {'user_post':user_post})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
	
def create_post(request):
	form = CreatePost(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				post = form.save(commit=False)
				post.username = request.user
				form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'create_post.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')