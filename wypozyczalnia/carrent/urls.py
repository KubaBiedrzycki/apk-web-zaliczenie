from django.urls import path
from . import views
# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome", views.welcome_view),
    path('', views.home, name='home'),  
    path('cars/', views.car_list, name='car_list'),
    path('clients/', views.client_list, name='client_list'),
    path('rentals/', views.rental_list, name='rental_list'),
    path('conditions/', views.condition_list, name='condition_list'),
    
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('rentals/<int:pk>/', views.rental_detail, name='rental_detail'),
    path('conditions/<int:pk>/', views.condition_detail, name='condition_detail'),
]