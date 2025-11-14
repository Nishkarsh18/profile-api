from django.urls import path

from profiles_api import views

urlpattern  = [
    path('hello-view/', views.HelloApiView.as_view()),
]