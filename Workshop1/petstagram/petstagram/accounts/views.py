from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, logout, get_user_model
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email','password1', 'password2']  # '__all__'
        labels ={
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repeat your password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Repeat your password'}),
        }


class RegisterUserView(generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
