from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register, name='register'),
    #path('home_user/',views.home_user, name='home_user'),

    
]