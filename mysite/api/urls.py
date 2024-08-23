# i created this file 

from django.urls import path
from . import views

urlpatterns = [
    path('sum/', views.SumView.as_view(), name='sum'),
    path('average/', views.AverageView.as_view(), name='average'),
    path('product/', views.ProductView.as_view(), name='product'),
]
