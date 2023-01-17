from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',login,name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('schedule-msg/', ScheduleMsgView.as_view(), name='schedule-msg'),

    path('allstudents/', VolunteersView.as_view(), name='allstudents'),
    path('add-secretary/', AddSecretaryView.as_view(), name='add-secretary'),

    path('logout', loginout, name='logout'),
    path('home/',home,name='home'),
]
