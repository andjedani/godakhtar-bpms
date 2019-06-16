from rest_framework import serializers

from inquiry.models import Inquiry, InquiryProducts


class InquiryProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryProducts
        fields = '__all__'


class InquirySerializer(serializers.ModelSerializer):
    inquiry_products = InquiryProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Inquiry
        fields = "__all__"
#                   "last_godakhtar_visit", "last_customer_visit",
#                   "comments", "verified", "branchs", "personnel", "key_persons")
#
#
# class CustomerShortListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ("id", "name", "english_name", "customer_no", "classification",
#                   "activity", "customer_size", "priority",)
