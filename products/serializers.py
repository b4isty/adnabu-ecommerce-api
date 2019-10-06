from rest_framework import serializers
from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    class Meta:
        model = Category
        fields = ["id", "name", ]


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for SubCategory model
    """
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ("out_of_stock",)


class CategoryTotalSerializer(serializers.Serializer):
    """
    Serializer to calculate sum of product prices
    """
    categories = serializers.ListField(child=serializers.IntegerField())

