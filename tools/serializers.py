from rest_framework import serializers


class ChoicesSerializer(serializers.Serializer):
    choices = serializers.ListField(
        child=serializers.DictField(
            id=serializers.CharField(),
            value=serializers.CharField()

        )
    )
