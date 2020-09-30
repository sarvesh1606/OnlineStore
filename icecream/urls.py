from django.contrib import admin
from django.urls import path
from icecream import views

urlpatterns = [

    path("",views.index, name='homepage'),
    path("home",views.home,name='homes'),
    path("contact",views.contact, name='contact'),
    path("login",views.login, name='login'),
    path("signup",views.signup, name='signup'),
    path("logout",views.logout, name='logout'),

]