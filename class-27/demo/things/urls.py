from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_things, name="all_things"),
    path('<int:pk>/', views.thing_detail, name="thing_detail"),
    path('create', views.thing_create, name="thing_create"),
    path('update/<int:pk>', views.thing_update, name="thing_update"),
    path('delete/<int:pk>', views.thing_delete, name="thing_delete"),
    
]