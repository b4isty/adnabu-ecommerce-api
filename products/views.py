from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product, Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from .permissions import IsOwnerUser, IsSuperUseOrReadOnly


class CategoryAPIView(ListCreateAPIView):
    """
    Class for get list and create Category
    """
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUseOrReadOnly,)
    queryset = Category.objects.all()


class SubCategoryAPIView(ListCreateAPIView):
    """
    Class for get list and create SubCategory
    """
    serializer_class = SubCategorySerializer
    permission_classes = (IsSuperUseOrReadOnly,)
    queryset = SubCategory.objects.all()


class ProductAPIView(ListCreateAPIView):
    """
    Class for get list and create Products
    """
    serializer_class = ProductSerializer
    permission_classes = (IsSuperUseOrReadOnly,)
    queryset = Product.objects.all()


class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class for get retrieve, update and delete Products
    """
    serializer_class = ProductSerializer
    permission_classes = (IsSuperUseOrReadOnly,)
    queryset = Product.objects.all()







