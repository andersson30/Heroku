from rest_framework import serializers
from proveedor.models import Proveedor, Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"