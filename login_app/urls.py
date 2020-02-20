from django.urls import path
from . import views


urlpatterns = [
    path('', views.wall),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('signin', views.index),
    path('message', views.message),
    path('comment', views.comment)
]