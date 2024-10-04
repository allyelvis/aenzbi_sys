from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='restaurant_pos_index'),
    # Add more paths and views as needed
]
