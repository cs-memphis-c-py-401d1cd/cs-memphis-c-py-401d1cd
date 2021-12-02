from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_things, name="all_things"),
    path('things/<int:pk>/', views.thing_detail, name="thing_detail")
]