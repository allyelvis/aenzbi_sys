from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounting_index'),
    # Add more paths and views as needed
]
