from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('signup/', views.signupuser, name='signupuser'),
]
