from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='video_generator_index'),
    # Add more paths and views as needed
]
