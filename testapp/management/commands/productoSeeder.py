from django.core.management.base import BaseCommand
from ecomerce.models import * 

class Command(BaseCommand):
    help = 'Todos los seeder'
    def handle(self, *args, **options):
        productos_data = [
            {
                'NombreProducto': 'iPhone 12 Pro mega',
                'idMarca': Marca.objects.get(pk=2),
                'idModelo': Modelo.objects.get(pk=1),
                'idColor': Color.objects.get(pk=3),
                'idTalla': Talla.objects.get(pk=2),
                'imagen': 'https://falabella.scene7.com/is/image/FalabellaPE/gsc_117080799_1009401_1?wid=1500&hei=1500&qlt=70',
                'PrecioVenta': 30000.00,

            },
            {
                'NombreProducto': 'Galaxy S21',
                'idMarca': Marca.objects.get(pk=2),
                'idModelo': Modelo.objects.get(pk=1),
                'idColor': Color.objects.get(pk=3),
                'idTalla': Talla.objects.get(pk=2),
                'imagen': 'https://falabella.scene7.com/is/image/FalabellaPE/gsc_117080799_1009401_1?wid=1500&hei=1500&qlt=70',
                'PrecioVenta': 30000.00,
            
            },
            {
                'NombreProducto': 'PlayStation 4',
                'idMarca': Marca.objects.get(pk=5),
                'idModelo': Modelo.objects.get(pk=5),
                'idColor': Color.objects.get(pk=3),
                'idTalla': Talla.objects.get(pk=2),
                'imagen': 'https://m.media-amazon.com/images/I/51+AvgQs50L._SL1500_.jpg',
                'PrecioVenta': 10000.00,
                
            },
        ]
        for producto_data in productos_data:
            try:
                Producto.objects.create(**producto_data)
                self.stdout.write(self.style.SUCCESS(f"Creada: {producto_data['NombreProducto']}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"No se pudo crear : {e}"))        