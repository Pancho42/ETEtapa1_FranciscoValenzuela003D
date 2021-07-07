from django.urls import path
from . import views

urlpatterns=[
    path('',views.Paginaprincipal, name='Paginaprincipal'),
    path('Productos/',views.Productos, name='Productos'),
    path('QuienesSomos/',views.QuienesSomos, name='QuienesSomos'),
    path('Registro/',views.Registro, name='Registro'),
    path('Despacho/',views.Despacho, name='Despacho'),
    path('Proveedores/',views.Proveedores, name='Proveedores'),
    path('CrearProveedores/',views.CrearProveedores, name='CrearProveedores'),
    path('ModProveedores/<id>',views.ModProveedores, name='ModProveedores'),
    path('eliminar/<id>',views.eliminar, name='eliminar'),
]