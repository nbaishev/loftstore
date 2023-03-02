from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Product
