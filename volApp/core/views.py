from .models import *
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from .forms import *
from django.contrib.auth import login as auth_login
# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@method_decorator(login_required(login_url='login'),name='dispatch')
class ProfileView(UpdateView):
    model = User
    fields = ['username','email','first_name','last_name','city']
    template_name = 'profile.html'
    success_url = '/home/'

    def get_object(self, queryset=None):
        return self.request.user


class ScheduleView(CreateView):
    model = ScheduleModel
    form_class = AddScheduleForm
    template_name = 'schedule.html'
    success_url = '/home/'

class ScheduleMsgView(ListView):
    model = ScheduleModel
    template_name = 'schedule-msg.html'


class VolunteersView(ListView):
    model = User
    template_name = 'allstudents.html'




class AddSecretaryView(CreateView):
    model = User
    form_class = AddSecretaryForm
    template_name = 'add-secretary.html'
    success_url = '/home/'


class Signup(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = '/home/'


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "GET":
            return render(request, 'login.html')
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                print('Something Wrong.!!')
    return redirect('login')

def loginout(request):
    logout(request)
    return redirect('login')