from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='invoicing_index'),
    # Add more paths and views as needed
]
