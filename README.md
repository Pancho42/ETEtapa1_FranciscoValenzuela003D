# ETEtapa1_FranciscoValenzuela003D
Etapa 1 del Examen Transversal

Creación Usuario oracle
create user c##proveedor identified by proveedor;
grant connect, resource to c##proveedor;
alter user c##proveedor default tablespace users quota unlimited on users;

SuperUsuario
User: admin
password: admin1234

PATH/URLS:
Index: http://127.0.0.1:8000/
Read/Update/Delete: http://127.0.0.1:8000/Proveedores/
Create: http://127.0.0.1:8000/CrearProveedores/
Admin: http://127.0.0.1:8000/admin/

La carpeta se llama exp3 pero es porque use el proyecto como base y no quise cambiarla por temor a generar algún error




