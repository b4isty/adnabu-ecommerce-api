from rest_framework import serializers
from  accounts.serializers import UserSerializer
from products.serializers import ProductSerializer
from .models import Cart, Order


class CartCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for create Cart instance
    """

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ("user", "active", "total_price")


class CartUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for update Cart instance
    """

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ("user", "active", "total_price")


class OrderSerializer(serializers.ModelSerializer):
    """
    serializer for Order model
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ("cart", "total")
        depth = 1

