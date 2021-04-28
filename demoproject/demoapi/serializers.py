from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Demonstration


class DemonstrationSerializer(ModelSerializer):

    def validate_index(self, value):
        print("validating index")
        if value < 0:
            raise ValidationError("index too small")
        return value

    def validate(self, attrs):
        print("validating object...", attrs)
        return attrs

    class Meta:
        model = Demonstration
        fields = ['id', 'name', 'index', 'value']
