from django.urls import path
from .views import CategoryAPIView, SubCategoryAPIView, ProductAPIView, ProductUpdateDestroyAPIView

app_name = "products"

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="category"),
    path("sub-categories/", SubCategoryAPIView.as_view(), name="subcategory"),
    path("products/", ProductAPIView.as_view(), name="list"),
    path("products/<int:pk>/", ProductUpdateDestroyAPIView.as_view(), name="modify"),
]
