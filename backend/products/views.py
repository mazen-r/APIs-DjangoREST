from typing import Generic
from rest_framework import authentication, generics, permissions
from api.authentication import TokenAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializers):
        title = serializers.validated_data.get('title')
        content = serializers.validated_data.get('content') or None
        if content is None:
            content = title
        serializers.save(content=content)
        authentication_classes = [
            authentication.SessionAuthentication,
            TokenAuthentication,
        ]
        permission_class = [permissions.IsAdminUser, IsStaffEditorPermission]  


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer