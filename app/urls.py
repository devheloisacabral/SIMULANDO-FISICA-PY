from django.urls import path
from . import views


urlpatterns = [
    path('', views.coders, name='coders'),
    path('servicos/', views.index, name='index'),
    path('lh', views.lh_simulator, name='lh'),
    path('lo', views.lo_simulator, name='lo'),
    path('calculator', views.calculator, name='calculator'),
    path('coders', views.coders, name='coders')
]