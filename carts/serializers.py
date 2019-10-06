from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import Cart


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



