from django.urls import path, include
from .views import *

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('cart/', CartView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]
