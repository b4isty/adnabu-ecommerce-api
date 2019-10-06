from django.urls import path
from .views import CategoryAPIView, CategoryUpdateDestroyAPIView, SubCategoryAPIView,\
    SubCategoryUpdateDestroyAPIView, ProductAPIView, ProductUpdateDestroyAPIView, CategoryTotalAPIView

app_name = "products"

urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="category"),
    path("categories/<int:pk>/", CategoryUpdateDestroyAPIView.as_view(), name="category_detail"),
    path("sub-categories/", SubCategoryAPIView.as_view(), name="subcategory"),
    path("sub-categories/<int:pk>/", SubCategoryUpdateDestroyAPIView.as_view(), name="subcategory_detail"),
    path("products/", ProductAPIView.as_view(), name="list"),
    path("products/<int:pk>/", ProductUpdateDestroyAPIView.as_view(), name="modify"),
    path("category-total/", CategoryTotalAPIView.as_view(), name="total")
]
