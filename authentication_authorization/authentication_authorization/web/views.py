from django.contrib.auth.models import User
from random import randint
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

UserModel = get_user_model()

@login_required
def index(request):
    suffix = randint(1, 1000)

    # Not a good idea
    # UserModel.objects.create(
    #     username=f'sisko_{suffix}',
    #     password='1123qwer',
    # )

    # Good Idea
    user = UserModel.objects.create_user(
        username=f'sisko_{suffix}',
        password='1123qwer',
    )
    auth_login(request, user)
    print(request.user)
    context = {
        "user": request.user,
        "permission": request.user.has_perm('web.view_user'),
    }
    return render(request, 'index.html', context)


def login(request):
    # Authentication
    user = authenticate(
        username='sisko_656',
        password='1123qwer'
    )
    # Authorization
    auth_login(request, user) # does request.user = user + other stuff
    print(f'Authenticated user: {user}')
    return redirect('index')


def user_logout(request):
    auth_logout(request)
    return redirect('index')


def test_login(request):
    user = UserModel.objects.get(username='sisko_656')
    user.set_password('1123qwer')
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()

    # Verify user attributes
    print(user.is_staff)  # Should be True
    print(user.is_active)  # Should be True
    print(user.is_superuser)  # Should be True
    print(user.check_password('1123qwer'))  # Should return True
    user = authenticate(username='sisko_21', password='1123qwer')
    if user is not None:
        auth_login(request, user)
        return HttpResponse("Logged in successfully")
    else:
        return HttpResponse("Failed to log in")