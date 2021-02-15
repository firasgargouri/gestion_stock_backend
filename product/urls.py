from django.urls import path, include
from .views import (ProductList, ProductCreate, ProductDetails, CategoryList, CategoryCreate,
                    CategoryDetails, SubCategoryList, SubCategoryCreate, SubCategoryDetails,)

app_name = 'product'

urlpatterns = [
    # products
    path('all/', ProductList.as_view(), name='ProductList'),
    path('create/', ProductCreate.as_view(), name='ProductCreate'),
    path('<int:pk>', ProductDetails.as_view(), name='ProductDetails'),

    # Categories
    path('category/all/', CategoryList.as_view(), name='CategoryList'),
    path('category/create/', CategoryCreate.as_view(), name='CategoryCreate'),
    path('category/<int:pk>', CategoryDetails.as_view(), name='CategoryDetails'),

    # SubCategories
    path('subcategory/all/', SubCategoryList.as_view(), name='SubCategoryList'),
    path('subcategory/create/', SubCategoryCreate.as_view(),
         name='SubCategoryCreate'),
    path('subcategory/<int:pk>', SubCategoryDetails.as_view(),
         name='SubCategoryDetails'),
]
