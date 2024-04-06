from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:pk>', views.order, name='clients_order'),
    path('client_all/<int:pk>/<int:dt>', views.client_products, name='clients_products'),
]