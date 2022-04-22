from typing import Generic
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializers):
        title = serializers.validated_data.get('title')
        content = serializers.validated_data.get('content') or None
        if content is None:
            content = title
        serializers.save(content=content)    


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer