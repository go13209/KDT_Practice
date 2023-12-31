from django.urls import path
from . import views

app_name = 'throw_catch'
urlpatterns = [
    path('', views.throw, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]