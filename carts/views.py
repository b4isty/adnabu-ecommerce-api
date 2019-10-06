from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Cart
from .serializers import CartCreateSerializer, CartUpdateSerializer
from products.models import Product

# Create your views here.


class CartAPIView(GenericAPIView):
    """
    Class for get and create Cart
    """
    serializer_class = CartCreateSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        cart_qs = Cart.objects.filter(active=True, user=request.user)
        if cart_qs:
            cart_obj = cart_qs.first()
            serializer = self.get_serializer(cart_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        # request.data["user"] = request.user.id
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




