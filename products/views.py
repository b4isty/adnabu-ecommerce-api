from django.db.models import Sum
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from .models import Product, Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, CategoryTotalSerializer
from .permissions import IsOwnerUser, IsSuperUseOrReadOnly



class CategoryAPIView(ListCreateAPIView):
    """
    Class for get list and create Category
    """
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUseOrReadOnly,)
    queryset = Category.objects.all()


class CategoryUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    class for retrieve, update and delete Category
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


class SubCategoryUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class for retrieve, update and delete SubCategory
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

    def list(self, request, *args, **kwargs):
        category = self.kwargs.get("category")
        if category:
            product_qs = Product.objects.filter(categories__id=category, out_of_stock=False)
            serializer = self.get_serializer(product_qs, many=True)
            return Response(serializer.data, status=200)
        return super(ProductAPIView, self).list(request, *args, **kwargs)


class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class for retrieve, update and delete Products
    """
    serializer_class = ProductSerializer
    permission_classes = (IsSuperUseOrReadOnly,)
    queryset = Product.objects.all()


class CategoryTotalAPIView(GenericAPIView):
    """
    Class to get sum of product prices
    """
    serializer_class = CategoryTotalSerializer
    permission_classes = (IsSuperUseOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        categories = serializer.data["categories"]
        total = Category.objects.filter(id__in=categories).aggregate(Sum("total"))["total__sum"]
        return Response(data={"total": total}, status=200)




