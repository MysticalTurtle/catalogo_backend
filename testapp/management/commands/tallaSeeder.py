from django.core.management.base import BaseCommand
from ecomerce.models import * 

class Command(BaseCommand):
    help = 'Todos los seeder'
    def handle(self, *args, **options):
        tallas_data = [
            {'NombreTalla': 'Talla S'},
            {'NombreTalla': 'Grande'},
            {'NombreTalla': 'Extragrande'},
            {'NombreTalla': 'Talla XL'},
        ]
        for talla_data in tallas_data:
            try:
                Talla.objects.create(**talla_data)
                self.stdout.write(self.style.SUCCESS(f"Creada: {talla_data['NombreTalla']}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"No se pudo crear : {e}"))        