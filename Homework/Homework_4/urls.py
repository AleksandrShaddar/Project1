from django.urls import path
from . import views

urlpatterns = [
    path('update_product/', views.update_product, name='update_product'),
]