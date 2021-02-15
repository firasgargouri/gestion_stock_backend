from django.urls import path, include
from .views import ProductList, ProductCreate

app_name = 'product'

urlpatterns = [
    # products
    path('all/', ProductList.as_view(), name='list'),
    path('create/', ProductCreate.as_view(), name='create'),

    # products
    path('all/', ProductList.as_view(), name='list'),
    path('create/', ProductCreate.as_view(), name='create'),

    # products
    path('all/', ProductList.as_view(), name='list'),
    path('create/', ProductCreate.as_view(), name='create'),
    # path('<int:pk>', ProductCreate.as_view(), name='create'),
]
