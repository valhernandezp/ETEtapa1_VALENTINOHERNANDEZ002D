from django.db import models


class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='id de categoria')
    nombreCategoria=models.CharField(max_length=50 ,verbose_name='Nombre de la categoria')

    def __str__(self):
        return (self.nombreCategoria)
    
class Proveedor(models.Model):
    idProveedor=models.CharField(max_length=10,primary_key=True,verbose_name='Id del proveedor')
    Nombre=models.CharField(max_length=50,verbose_name='Nombre del proveedor')
    Telefono=models.CharField(max_length=12,verbose_name='Telefono del proveedor')
    Direccion=models.CharField(max_length=50,verbose_name='Direccion del proveedor')
    Email=models.CharField(max_length=40,verbose_name='Email del proveedor')
    Pais=models.CharField(max_length=20,verbose_name='Pais del proveedor')
    Contraseña=models.CharField(max_length=20,verbose_name='Contraseña del proveedor')
    Moneda=models.IntegerField(verbose_name='Tipo de moneda (dolar o pesos chilenos)')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return(self.idProveedor)