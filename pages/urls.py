from django.urls import path
from . import views 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hosts/', views.hosts, name='hosts'),
    path('organization/', views.organization , name = 'organization'),
    path('fees/', views.fees, name='fees'),
    path('contacts/', views.contacts, name='contacts'),
    path('venue/', views.venue, name='venue'),
    path('timeline/', views.timeline, name='timeline'),

    path('topics/', views.topics ,name = 'topics'),
    path('Accomodations/', views.Accommodations , name='Accommodations'),
    path('themes/', views.Conference_Themes_and_Topics, name='themes'),
    path('paperformat/', views.paperformat, name='paperformat'),
    path('photos/', views.photos, name='photos'),
    path('invited_speaker/', views.invited_speaker, name='invited_speaker'),
    path('keynote_speaker/', views.keynote_speaker, name='keynote_speaker'),

    path('program/', views.program , name="program"),
    path('profile/', views.profile , name="profile"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("information/", views.information , name = "information"),
    path("logout/", views.unsubscribe_session, name="logout"),


    path('conference_outline/', views.conference_outline, name='conference_outline'),
    path('daily_program/', views.daily_program, name='daily_program'),

    path("regsteration/", views.registeration , name='registeration'),
    path("abstract/", views.abstract , name='abstract'),

]
