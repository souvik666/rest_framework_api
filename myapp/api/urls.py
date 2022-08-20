from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem)
]