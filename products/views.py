from rest_framework import viewsets

from .serializers import ProductSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
