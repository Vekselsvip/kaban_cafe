from django.urls import path
from .views import reservations_list, update_reservations


urlpatterns = [
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>', update_reservations, name='update_reserve')
]