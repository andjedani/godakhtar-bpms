import datetime
import json
import os

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

import tools
from products import models, serializers


@api_view(['GET',])
def product_types(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        serializer = tools.serializers.ChoicesSerializer(models.Product.PRODUCT_TYPE_CHOICES, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects
    serializer_class = serializers.AttributeSerializer

    def get_object(self):
        product_id = self.kwargs.get('product_id', None)
        product = models.Product(pk=product_id)
        return get_object_or_404(models.Attribute, product=product)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects
    serializer_class = serializers.ProductSerializer

    def get_object(self):
        product_name = self.kwargs.get('product_name', None)
        if product_name:
            return get_object_or_404(models.Product, product_name=product_name )
        return super().get_object()

    def initial(self, request, *args, **kwargs):
        log_data = {
            'timestamp': datetime.datetime.now().timestamp(),
            'user': request.user.pk,
            'remote_address': request.META['REMOTE_ADDR'],
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.data,
            'request_query_params': request.query_params,
            'request_auth': request.auth,
        }
        if not os.path.exists('log'):
            os.makedirs('log')

        with open('log/log.json', 'a+') as f:
            json.dump(log_data, f, sort_keys=True, indent=4)
        viewsets.ModelViewSet.initial(self, request, *args, **kwargs)
