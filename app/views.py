from time import strftime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
import os
from datetime import date, datetime
from django.views.csrf import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth

from .models import DiscordBot


today = datetime.now()
today_format = today.strftime("%b. %d, %Y")

# Create your views here.
@login_required
def index(request):
    context = {
        'today': today_format,
    }
    return render(request, 'index.html', context)

# @login_required
# def discordBot(request):
#     if request.method == 'POST':
#         boolean = request.POST['boolean']
        
#         if boolean == True:
#             # Zet de bot aan (code van bot.py)
#             return ""
#         else:
#             # Zet bot uit

# -----------------------------
# Auth
def login(request):
    return render(request, 'login.html', {})

def loginpost(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Succesfully logged out')
    return redirect('index')
# Auth
# -----------------------------