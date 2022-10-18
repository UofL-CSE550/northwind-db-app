from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('products', views.product_list),
    path('products/<int:id>', views.product_detail),
    path('orders', views.order_list),
    path('orders/<int:id>', views.order_detail),
    path('', views.index)
]