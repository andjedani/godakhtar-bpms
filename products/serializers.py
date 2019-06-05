from rest_framework import serializers
from products.models import Attribute, AttributeChoices, Product


class AttributeChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeChoices
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    attribute_choices = AttributeChoicesSerializer(many=True)

    class Meta:
        model = Attribute
        fields = ('id', 'name', 'type', 'validator', 'attribute_choices')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
