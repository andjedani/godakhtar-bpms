import datetime
import json
import os

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from inquiry import serializers
from inquiry.models import Inquiry, InquiryProducts
from products.models import Product


@api_view(['POST', ])
def add_product_to_inquiry(request, inquiry_id):
    product_type = request.data['product_type']
    product_size = request.data['product_size']
    product_class = request.data['product_class']
    product_connection = request.data['product_connection']
    quantity = int(str(request.data['quantity']))

    product, created = Product.objects.get_or_create(product_type=product_type,
                                                     product_size=product_size,
                                                     product_class=product_class,
                                                     product_connection=product_connection)
    inquiry = Inquiry.objects.get(pk=inquiry_id)
    InquiryProducts.objects.create(inquiry=inquiry, product=product, quantity=quantity)
    # inq_ser = serializers.InquirySerializer(Inquiry.objects.get(pk=inquiry_id))
    resp = {"created": str(created)}
    return Response(resp, status.HTTP_200_OK)


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects
    serializer_class = serializers.InquirySerializer

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
