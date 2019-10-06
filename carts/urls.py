from django.urls import path
from .views import CartAPIView, CartRetrieveUpdateAPIView, CartDeleteProductAPIView

app_name = "carts"

urlpatterns = [
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("cart/update/<int:pk>/", CartRetrieveUpdateAPIView.as_view(), name="update"),
    path("cart/delete-product/<int:pk>/", CartDeleteProductAPIView.as_view(), name="delete"),

]
