from django.core.management.base import BaseCommand
from ecomerce.models import *

class Command(BaseCommand):
    help = 'Todos los seeder'
    def handle(self, *args, **options):
        modelos_data = [
            {'NombreModelo': 'iPhone'},
            {'NombreModelo': 'MacBook'},
            {'NombreModelo': 'Galaxy S'},
            {'NombreModelo': 'Ropa deportiva'},
            {'NombreModelo': 'PlayStation'},
        ]
        for modelo_data in modelos_data:
            try:
                Modelo.objects.create(**modelo_data)
                self.stdout.write(self.style.SUCCESS(f"Modelo creada: {modelo_data['NombreModelo']}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"No se pudo crear: {e}"))        