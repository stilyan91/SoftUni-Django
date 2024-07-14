from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_password_management.app_auth.urls')),
    path('', include('user_password_management.web.urls')),
]
