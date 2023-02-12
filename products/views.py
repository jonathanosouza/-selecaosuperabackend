from rest_framework import viewsets
from products.models import Products
from products.serializer import ProductsSerializer



class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer