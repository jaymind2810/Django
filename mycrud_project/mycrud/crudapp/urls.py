from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_registration, name='add_registration'),
    path('list/', views.registration_list, name='registration_list'),
]