from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page listing all cars
    path('car/add_car/', views.add_car, name='add_car'),  # Page to add a new car
    path('car/<int:id>/', views.car_detail, name='car_detail'),  # Detail view for a specific car
    path('car/edit_car/<int:id>/', views.edit_car, name='edit_car'),  # Page to edit an existing car
]
