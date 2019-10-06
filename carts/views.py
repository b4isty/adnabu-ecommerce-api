from datetime import timedelta

from django.db.models import Count, Sum, Max
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import UserSerializer
from .models import Cart, Order
from .serializers import CartCreateSerializer, CartUpdateSerializer, OrderSerializer
from products.models import Product

User = get_user_model()

class CartAPIView(GenericAPIView):
    """
    Class for get and create Cart
    """
    serializer_class = CartCreateSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        cart_qs = Cart.objects.filter(active=True, user=request.user)
        if cart_qs:
            cart_qs = cart_qs.first()
            serializer = self.get_serializer(cart_qs)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """
    class for retrieve and update Cart
    """
    serializer_class = CartUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cart_qs = Cart.objects.filter(user=self.request.user, active=True)
        if cart_qs:
            return cart_qs
        Cart.objects.create(user=self.request.user)
        cart_qs = Cart.objects.filter(user=self.request.user, active=True)
        return cart_qs


class CartDeleteProductAPIView(DestroyAPIView):
    """
    Class for remove products from Cart
    """
    serializer_class = CartUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cart_qs = Cart.objects.filter(user=self.request.user, active=True)
        return cart_qs

    def delete(self, request, *args, **kwargs):
        print(kwargs.get("pk"))
        prod_obj = get_object_or_404(Product, pk=kwargs.get('pk'))
        cart_queryset = self.get_queryset().filter()
        print("**", cart_queryset)
        if cart_queryset.count():
            active_cart = cart_queryset.first()
            active_cart.products.remove(prod_obj)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OrderAPIView(GenericAPIView):
    """
    Class for Order
    """
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        order_qs = Order.objects.filter(user=request.user)
        if order_qs:
            serializer = self.get_serializer(order_qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        cart_qs = Cart.objects.filter(user=request.user, active=True)
        if cart_qs:
            cart_obj = cart_qs.first()
            cart_obj.active = False
            cart_obj.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, cart=cart_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise Response(status=status.HTTP_404_NOT_FOUND)


class UserStatisticsAPIView(GenericAPIView):
    """
    class to get maximum order and maximum total order value users
    """
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        max_order_users = User.objects.filter(order__created_at__gte=timezone.now() - timedelta(days=30)\
                                              ).annotate(order_count=Count("order")).order_by("-order_count")
        max_order_users = self.get_serializer(max_order_users, many=True).data
        data = {"max_order_users": max_order_users}
        max_value_users = User.objects.filter(order__created_at__gte=timezone.now() - timedelta(days=30)\
                                              ).annotate(value_sum=Sum("order__total")).order_by("-value_sum")

        max_value_users = self.get_serializer(max_value_users, many=True).data
        data["top_value_users"] = max_value_users
        return Response(data, status=200)




