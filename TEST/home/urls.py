from django.contrib import admin
from django.urls import path, include
from home import views


# SET THE NAMESPACE!
app_name = 'home'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('', views.contact),
]