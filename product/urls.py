from django.urls import path, include
from .views import (ProductList, ProductCreate, CategoryList, SubCategoryList,)

app_name = 'product'

urlpatterns = [
    # products
    path('all/', ProductList.as_view(), name='ProductList'),
    path('create/', ProductCreate.as_view(), name='create'),

    # Categories
    path('categories/all/', CategoryList.as_view(), name='CategoryList'),
    path('create/', ProductCreate.as_view(), name='create'),

    # SubCategories
    path('subCategories/all/', SubCategoryList.as_view(), name='SubCategoryList'),
    path('create/', ProductCreate.as_view(), name='create'),
    # path('<int:pk>', ProductCreate.as_view(), name='create'),
]
