from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mu', views.mu_simulator, name='mu'),
    path('muv', views.muv_simulator, name='muv'),
    path('mc', views.mc_simulator, name='mc'),
    path('lh', views.lh_simulator, name='lh'),
    path('lo', views.lo_simulator, name='lo'),
    path('calculator', views.calculator, name='calculator'),
    path('coders', views.coders, name='coders')
]