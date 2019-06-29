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
    product_type = str(request.data['product_type'])
    product_size = str(request.data['product_size'])
    product_class = str(request.data['product_class'])
    product_connection = request.data['product_connection']
    quantity = int(str(request.data['quantity']))

    product, created = Product.objects.get_or_create(product_type=product_type,
                                                     product_size=product_size,
                                                     product_class=product_class,
                                                     product_connection=product_connection)

    inquiry = Inquiry.objects.get(pk=inquiry_id)
    # TODO: Check if this inquiry already has this product or not?
    qs = InquiryProducts.objects.filter(inquiry=inquiry, product=product)
    already_exists = (len(qs) > 0)
    if already_exists:
        resp = {"already_exists": already_exists, "existing_id": qs[0].pk, "existing_quantity": qs[0].quantity}
    else:
        inq_prod = InquiryProducts.objects.create(inquiry=inquiry, product=product, quantity=quantity)
        resp = {"created": str(created), "added_id": inq_prod.pk, }
    # inq_ser = serializers.InquirySerializer(Inquiry.objects.get(pk=inquiry_id))
    return Response(resp, status.HTTP_200_OK)


@api_view(['DELETE', ])
def delete_product_from_inquiry(request, inquiry_id):
    product_id = int(str(request.data['product_id']))
    product = Product.objects.get(pk=product_id)
    inquiry = Inquiry.objects.get(pk=inquiry_id)
    inq_prod = InquiryProducts.objects.get(inquiry=inquiry, product=product)
    deleting_row_id = inq_prod.pk
    inq_prod.delete()
    # inq_ser = serializers.InquirySerializer(Inquiry.objects.get(pk=inquiry_id))
    resp = {"deleted": True, "deleted_id": deleting_row_id}
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
