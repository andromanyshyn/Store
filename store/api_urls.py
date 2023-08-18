from django.urls import include, path


urlpatterns = [
    path("products/", include("api_products.urls")),
    path("carts/", include("api_cart.urls")),
]
