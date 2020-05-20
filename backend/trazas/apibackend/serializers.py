# serializers.py
from rest_framework import serializers

from .models import FrezHhzTc9920200321

class FrezHhzTc9920200321Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrezHhzTc9920200321
        fields = ('st', 'et', 'sr', 'datatype', 'tracebuf')