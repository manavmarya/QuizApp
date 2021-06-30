from django.urls import path
from .views import view_register, view_profile

app_name = 'users'
urlpatterns = [
                path('register/', view_register, name='view_register'),
                path('profile/', view_profile, name='view_profile'),
              ]

