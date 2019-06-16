from rest_framework import serializers

from inquiry.models import Inquiry, InquiryProducts


class InquiryProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryProducts
        fields = '__all__'


# class PersonnelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Personnel
#         fields = '__all__'
#
#
# class KeyPersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KeyPerson
#         fields = '__all__'
#
#
class InquirySerializer(serializers.ModelSerializer):
    inquiry_products = InquiryProductsSerializer(many=True)
    # personnel = PersonnelSerializer(many=True)
    # key_persons = KeyPersonSerializer(many=True)
    # customer = CustomerSerializer

    class Meta:
        model = Inquiry
        fields = "__all__"
        # "financial_code", "national_id", "registration_no",
        # "classification", "activity", "customer_size", "priority",
        # "oil_section", "gas_section", "pertrochemical_section", "refinery_section", "plant_section",
        # "ownership", "owner",
        # "deal_type_gate", "deal_type_globe", "deal_type_check", "deal_type_ball", "deal_type_butterfly",
        # "deal_type_repair_service", "deal_type_spare_parts", "deal_type_other", "deal_type_maintenance",
        # "deal_worth", "deal_history",
        # "mechanism",
        # "deal_comments",
        # "inquiry_history",
        # "website", "email",
        # "acquainted_expo", "acquainted_website", "acquainted_vendor", "acquainted_other",
        # "acquainted_recommended",
#                   "last_godakhtar_visit", "last_customer_visit",
#                   "comments", "verified", "branchs", "personnel", "key_persons")
#
#
# class CustomerShortListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ("id", "name", "english_name", "customer_no", "classification",
#                   "activity", "customer_size", "priority",)
