from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from .forms import CustomUserCreationForm
from .models import CustomUser
from django import forms
from django.forms import CharField, Form, PasswordInput
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def register1(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})



def my_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            print('AHA')
    else: 
        form = UserLoginForm()
    return render(request, 'users/login-form.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def overseer(request):
    context = {
        'allUsers' : CustomUser.objects.all() 
    }
    return render(request, 'users/overseer.html', context=context)


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/overseer.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'allUsers'


class UsersUpdateView(LoginRequiredMixin,  UpdateView):
    form_class = UserUpdateForm
    model = CustomUser
    template_name = 'users/customuser_update_form.html'
    # template_name = 'users/customuser_form.html'
    success_url = '/overseer'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     CustomUser = self.get_object()
    #     if CustomUser.isAdmin():
    #         return True
    #     else:
    #         return False

class UsersCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    success_url = '/'
    fields = fields = ['username','first_name','last_name', 'email', 'website', 'password']
    def form_valid(self, form):
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

class UsersDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = '/'
