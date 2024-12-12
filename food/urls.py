from . import views
from django.urls import path

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
]
