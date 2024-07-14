from django.contrib.auth.views import LoginView
from django.urls import path

from user_password_management.app_auth.views import RegisterView, LogoutView, LoginUserView, UsersListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UsersListView.as_view(), name='user_list'),

]


# aaaa1234