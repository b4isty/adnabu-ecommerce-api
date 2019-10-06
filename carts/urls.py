from django.urls import path
from .views import CartAPIView, CartRetrieveUpdateAPIView, CartDeleteProductAPIView, OrderAPIView, UserStatisticsAPIView

app_name = "carts"

urlpatterns = [
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("cart/update/<int:pk>/", CartRetrieveUpdateAPIView.as_view(), name="update"),
    path("cart/delete-product/<int:pk>/", CartDeleteProductAPIView.as_view(), name="delete"),
    path("order/", OrderAPIView.as_view(), name="order"),
    path("statistics/", UserStatisticsAPIView.as_view(), name="stats")

]
