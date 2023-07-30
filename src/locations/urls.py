from django.urls import path
from . import views

urlpatterns = [
    path('add_region', views.RegionCreateView.as_view(), name='add_region')
]
