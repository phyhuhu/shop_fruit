from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('queue/', views.createQ, name='queue'),
    path('schedule/', views.createS, name='schedule'),
]

