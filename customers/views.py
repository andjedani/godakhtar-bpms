from customers import models,serializers
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects
    serializer_class = serializers.CustomerSerializer


