from django.db import models
from django.core.validators import *

# Create your models here.

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    NombreMarca = models.CharField(max_length=200,null=False, validators=[
            MinLengthValidator(limit_value=3, message="La longitud mínima debe ser de al menos 3 caracteres.")
        ]
    )

class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True)
    NombreModelo = models.CharField(max_length=200,null=False, validators=[
            MinLengthValidator(limit_value=3, message="La longitud mínima debe ser de al menos 3 caracteres.")
        ]
    )

class Color(models.Model):
    idColor = models.AutoField(primary_key=True)
    NombreColor = models.CharField(max_length=200,null=False, validators=[
            MinLengthValidator(limit_value=3, message="La longitud mínima debe ser de al menos 3 caracteres.")
        ]
    )

class Talla(models.Model):
    idTalla = models.AutoField(primary_key=True)
    NombreTalla = models.CharField(max_length=200,null=False, validators=[
            MinLengthValidator(limit_value=3, message="La longitud mínima debe ser de al menos 3 caracteres.")
        ]
    )

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    NombreProducto = models.CharField(max_length=200,null=False, validators=[
            MinLengthValidator(limit_value=3, message="La longitud mínima debe ser de al menos 3 caracteres.")
        ]
    )
    idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    idModelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='productos')
    idColor = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='productos')
    idTalla = models.ForeignKey(Talla, on_delete=models.CASCADE, related_name='productos')
    imagen = models.URLField(
        max_length=800,
        null=False,
        validators=[URLValidator(message="URL Inválida.")]
    )
    PrecioVenta = models.DecimalField( max_digits=9, decimal_places=2, validators=[
            MinValueValidator(limit_value=0, message="El precio de venta debe ser al menos 0."),
            MaxValueValidator(limit_value=999999, message="El precio de venta no puede ser superior a 999,999."),
        ]
    )
