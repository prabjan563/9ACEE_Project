from django.urls import path
from . import views
from .views import PaperSubmissionView, download_submission

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hosts/', views.hosts, name='hosts'),
    path('fees/', views.fees, name='fees'),
    path('contacts/', views.contacts, name='contacts'),
    path('venue/', views.venue, name='venue'),
    path('Accomodations/', views.Accommodations , name='Accommodations'),
    path('themes/', views.Conference_Themes_and_Topics, name='themes'),
    path('paperformat/', views.paperformat, name='paperformat'),
    path('photos/', views.photos, name='photos'),
    path('invited_speaker/', views.invited_speaker, name='invited_speaker'),
    path('keynote_speaker/', views.keynote_speaker, name='keynote_speaker'),
    path('program/', views.program , name="program"),

    # Paper Submission URLs
    path('paper/submit/', PaperSubmissionView.as_view(), name='paper-submit'),
    path('paper/download/<int:pk>/', download_submission, name='paper-download'),
]
