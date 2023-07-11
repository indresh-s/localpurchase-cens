from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("/")
		else:
			messages.info(request,'invalid user / credentials')
			return redirect('login')
	else:
		return render(request,'registeruser/login.html')