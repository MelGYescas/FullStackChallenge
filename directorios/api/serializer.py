from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer

class UserCustomerSerializer(serializers.ModelSerializer):
    nombre = serializers.SerializerMethodField()
  

    class Meta:
        model = Customer
        fields = ('nombre', 'telefono', 'correo')

    def get_nombre(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
