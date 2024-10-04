from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='crm_index'),
    # Add more paths and views as needed
]
