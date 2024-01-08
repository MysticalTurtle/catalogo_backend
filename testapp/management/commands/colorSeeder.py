from django.core.management.base import BaseCommand
from ecomerce.models import *  

class Command(BaseCommand):
    help = 'Todos los seeder'
    def handle(self, *args, **options):
        colors_data = [
            {'NombreColor': 'Rojo'},
            {'NombreColor': 'Gris'},
            {'NombreColor': 'Azul'},
            {'NombreColor': 'Negro'},
            {'NombreColor': 'Verde'},
        ]
        for color_data in colors_data:
            try:
                Color.objects.create(**color_data)
                self.stdout.write(self.style.SUCCESS(f"Marca creada: {color_data['NombreColor']}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"No se pudo crear la marca: {e}"))        