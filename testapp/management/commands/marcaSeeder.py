from django.core.management.base import BaseCommand
from ecomerce.models import * 

class Command(BaseCommand):
    help = 'Todos los seeder'
    def handle(self, *args, **options):
        marcas_data = [
            {'NombreMarca': 'No Especifica'},
            {'NombreMarca': 'Apple'},
            {'NombreMarca': 'Samsung'},
            {'NombreMarca': 'Nike'},
            {'NombreMarca': 'Sony'},
        ]
        for marca_data in marcas_data:
            try:
                Marca.objects.create(**marca_data)
                self.stdout.write(self.style.SUCCESS(f"Marca creada: {marca_data['NombreMarca']}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"No se pudo crear la marca: {e}"))        