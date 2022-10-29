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

from app.bots.bot1 import turnOn

today = datetime.now()
today_format = today.strftime("%b. %d, %Y")

# Create your views here.
@login_required
def index(request):
    discord_bots = DiscordBot.objects.all().values()
    context = {
        'discord_bots': discord_bots,
        'today': today_format,
    }
    return render(request, 'index.html', context)

@login_required
def botOn(request, id):
    discord_bot = DiscordBot.objects.get(id=id)

    discord_bot.running = True
    discord_bot.save()

    # code here to run the bot, when you run it now using the turnOn() function, the terminal will halt and you will get an infinte loading page

    return HttpResponseRedirect(reverse('index'))

@login_required
def botOff(request, id):
    discord_bot = DiscordBot.objects.get(id=id)

    discord_bot.running = False
    discord_bot.save()

    # code here to turn the bot off,
    # possible fix: https://stackoverflow.com/questions/54561531/how-would-i-create-a-command-to-shutdown-my-discord-py-bot

    return HttpResponseRedirect(reverse('index'))

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