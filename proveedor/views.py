from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from proveedor.serializers import ProveedorSerializer
from proveedor.models import Proveedor, Proveedor

# Create your views here.
class ListProveedorAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class CreateProveedorAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class UpdateProveedorAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class DeleteProveedorAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer