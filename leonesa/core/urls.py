from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('other/', views.other, name='other'),
    path('mision/', views.mision, name='mision'),
    path('aboutme/', views.historia, name='history'),
    path('consultorio/', views.visit, name='visit'),
]