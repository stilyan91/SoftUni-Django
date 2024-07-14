from django import views
from django.urls import path
from .views import index, login, user_logout, test_login

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('test-login/', test_login),
]

'''
Auth flow: 

The user sends the credentials to a system 
    - username & password, phone_number + sms_code, authentication app
    
Authentication
After authentication, the system authorizes the user

 
'''

'''
Web1(web app)
    - softuni_key = '4123-4213-5421'
Web2(web app)
    - softuni_key = '4123-4213-5421'
'''

# 1123qwer

'''
DB -> pbkdf2_sha256$720000$IAEod8UITygvQeU7PHIIDo$0bgNZJH2ro6u
1123qwer -> pbkdf2_sha256$720000$IAEod8UITygvQeU7PHIIDo$0bgNZJH2ro6u

'''

# NEVER name your auth app with 'auth'
# Name it 'app_auth', 'my_auth' ....
