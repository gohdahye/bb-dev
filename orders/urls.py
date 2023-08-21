from django.urls import path
from .views import order_create, order_list
app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('list/', order_list, name='order_list'),
]
