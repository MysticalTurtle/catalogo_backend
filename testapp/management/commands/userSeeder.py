from django.core.management.base import BaseCommand
from ecomerce.models import * 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class Command(BaseCommand):
    help = 'Todos los seeder'
    def handle(self, *args, **options):
        usuarios_data = [
            {
                'username': 'usuario_normal',
                'email': 'usuario_normal@example.com',
                'password': 'usuario_normal',
                'is_staff': False,
                'is_superuser': False,
            },
            {
                'username': 'admin_usuario',
                'email': 'admin_usuario@example.com',
                'password': 'admin_usuario',
                'is_staff': True,
                'is_superuser': False,
            },
            {
                'username': 'admin_superusuario',
                'email': 'admin_superusuario@example.com',
                'password': 'admin_superusuario',
                'is_staff': True,
                'is_superuser': False,
            },

        ]

        for usuario_data in usuarios_data:
            try:
                # Crea el usuario y asigna la contraseña usando set_password
                usuario = User.objects.create_user(
                    username=usuario_data['username'],
                    email=usuario_data['email'],
                    password=usuario_data['password'],
                    is_staff=usuario_data['is_staff'],
                    is_superuser=usuario_data['is_superuser'],
                )
                usuario.set_password(usuario_data['password'])
                usuario.save()

                self.stdout.write(self.style.SUCCESS(f"Creado usuario: {usuario.username}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"No se pudo crear el usuario: {e}"))