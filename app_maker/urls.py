from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_maker_index'),
    # Add more paths and views as needed
]
