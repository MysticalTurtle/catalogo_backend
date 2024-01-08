# Generated by Django 4.2.9 on 2024-01-08 06:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                ("idColor", models.AutoField(primary_key=True, serialize=False)),
                (
                    "NombreColor",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=3,
                                message="La longitud mínima debe ser de al menos 3 caracteres.",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                ("idMarca", models.AutoField(primary_key=True, serialize=False)),
                (
                    "NombreMarca",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=3,
                                message="La longitud mínima debe ser de al menos 3 caracteres.",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Modelo",
            fields=[
                ("idModelo", models.AutoField(primary_key=True, serialize=False)),
                (
                    "NombreModelo",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=3,
                                message="La longitud mínima debe ser de al menos 3 caracteres.",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Talla",
            fields=[
                ("idTalla", models.AutoField(primary_key=True, serialize=False)),
                (
                    "NombreTalla",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=3,
                                message="La longitud mínima debe ser de al menos 3 caracteres.",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("idProducto", models.AutoField(primary_key=True, serialize=False)),
                (
                    "NombreProducto",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=3,
                                message="La longitud mínima debe ser de al menos 3 caracteres.",
                            )
                        ],
                    ),
                ),
                (
                    "imagen",
                    models.URLField(
                        max_length=800,
                        validators=[
                            django.core.validators.URLValidator(message="URL Inválida.")
                        ],
                    ),
                ),
                (
                    "PrecioVenta",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=9,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0,
                                message="El precio de venta debe ser al menos 0.",
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=999999,
                                message="El precio de venta no puede ser superior a 999,999.",
                            ),
                        ],
                    ),
                ),
                (
                    "idColor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="ecomerce.color",
                    ),
                ),
                (
                    "idMarca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="ecomerce.marca",
                    ),
                ),
                (
                    "idModelo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="ecomerce.modelo",
                    ),
                ),
                (
                    "idTalla",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productos",
                        to="ecomerce.talla",
                    ),
                ),
            ],
        ),
    ]
