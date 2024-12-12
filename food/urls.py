from . import views
from django.urls import path

urlpatterns = [
    path('', views.food_list, name='food_list'),
]
