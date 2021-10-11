from django.urls import path
from proveedor import views

urlpatterns = [
    path("",views.ListProveedorAPIView.as_view(),name="proveedor_list"),
    path("create/", views.CreateProveedorAPIView.as_view(),name="proveedor_create"),
    path("update/<int:pk>/",views.UpdateProveedorAPIView.as_view(),name="update_proveedor"),
    path("delete/<int:pk>/",views.DeleteProveedorAPIView.as_view(),name="delete_proveedor")
]