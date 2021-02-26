from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about,name='about'),
    path('Liberte/',views.Liberte,name=('Liberte')),
    path('Elwatan/',views.elwatan,name=('Elwatan')),
    path('APS/',views.aps,name=('APS')),
    path('TSA/',views.tsa,name=('TSA')),
    path('reflexion/',views.reflexion,name=('reflexion')),
    path('lnr_dz/',views.lnr_dz,name=('lnr_dz')),
    path('lesoirdalgerie/',views.lesoirdalgerie,name=('lesoirdalgerie')),
    path('lequotidien/',views.lequotidien,name=('lequotidien')),
    path('jeune/',views.jeune,name=('jeune')),
    path('elmoudjahid/',views.elmoudjahid,name=('elmoudjahid')),
    path('dzfoot/',views.dzfoot,name=('dzfoot')),   
    path('competition/',views.competition,name=('competition')), 
    path('capouest/',views.capouest,name=('capouest')),
    path('bejaia/',views.bejaia,name=('bejaia')),
    
]

