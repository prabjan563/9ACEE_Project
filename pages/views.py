from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Photo , Notice , Post, Video
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .forms import SubscribeForm


def home(request):
    return render(request, 'pages/index.html')

def subscribe(request):
    # Check if user is already subscribed (has session)
    if request.session.get('is_subscribed'):
        return redirect('information')
    
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            # Set session to remember this user is subscribed
            request.session['is_subscribed'] = True
            request.session['subscriber_email'] = subscriber.email
            request.session['subscriber_name'] = subscriber.name
            messages.success(request, f'Welcome {subscriber.name}! You are now subscribed.')
            return redirect('information')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SubscribeForm()
    
    return render(request, 'pages/subscribe.html', {'form': form})


def information(request):
    # Check if user is subscribed
    if not request.session.get('is_subscribed'):
        messages.warning(request, 'Please subscribe to access this page.')
        return redirect('subscribe')
    
    notice = Notice.objects.filter(is_active=True).order_by('-created_at').first()
    posts = Post.objects.all().order_by('-created_at')[:10]
    videos = Video.objects.all().order_by('-created_at')[:5]
    
    # Get subscriber name from session
    subscriber_name = request.session.get('subscriber_name', 'Subscriber')

    return render(request, 'pages/information.html', {
        'notice': notice,
        'posts': posts,
        'videos': videos,
        'subscriber_name': subscriber_name,
    })


# Optional: Add this view if you want a logout/unsubscribe option
def unsubscribe_session(request):
    request.session.flush()  # Clear all session data
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def hosts(request):
    return render(request, 'pages/hosts.html')

def organization(request):
    return render(request, 'pages/organization.html')

def fees(request):
    return render(request, 'pages/fees.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

def profile(request):
    return render(request , 'pages/profile.html')

def venue(request):
    return render(request , 'pages/venue.html' )

def topics(request):
    return render(request , 'pages/topics.html')

def Accommodations(request):
    return render(request , 'pages/accommodations.html' )

def Conference_Themes_and_Topics(request):
    return render(request,'pages/themes.html')

def keynote_speaker(request):
    return render(request, 'pages/keynote_speaker.html')

def invited_speaker(request):
    return render(request, 'pages/invited_speaker.html')

def program(request):
    return render(request,'pages/program.html')

def paperformat(request):
    return render(request , 'pages/paper_format_and_agenda.html')

def photos(request):
    all_photos = Photo.objects.all()
    return render(request, 'pages/photos.html', {'photos': all_photos})


def registeration(request):
    return render(request, 'pages/registeration.html' )

def abstract(request):
    return render(request, 'pages/abstract.html' )