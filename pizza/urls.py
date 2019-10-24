from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('pizze/', views.pizze, name='pizze'),
]
