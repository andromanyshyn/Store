from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('products/', views.ListProductsView.as_view(), name='products'),
    path('categories/<int:category_id>/', views.ListProductsView.as_view(), name='categories_products'),
    path('products/<int:product_id>/', views.get_basket, name='basket'),
    path('basket-remove/<int:basket_object_id>/<int:user_id>/', views.remove_basket, name='remove_basket'),
]
