from django.urls import path
from . views import base_app_views, contact_views

app_name = 'base_app'

urlpatterns = [
    path('', base_app_views, name='base_app_views'),
    path('contact/', contact_views, name='contact')
]