# from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', views.accueil), #path('', views.index),
    url('presentation/', views.presentation, name='presentation'),
]