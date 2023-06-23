from django.urls import path
from . import views

urlpatterns = [
    path('lecturas/', views.posts, name='lecturas'),
]