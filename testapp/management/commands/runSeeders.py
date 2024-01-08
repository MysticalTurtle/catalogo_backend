from django.core.management.base import BaseCommand
from testapp.management.commands import colorSeeder,marcaSeeder,modeloSeeder,tallaSeeder,productoSeeder,userSeeder

class Command(BaseCommand):
    help = 'Ejecuta todos los seeders'

    def handle(self, *args, **options):
        colorSeeder.Command().handle()
        marcaSeeder.Command().handle()
        modeloSeeder.Command().handle()
        tallaSeeder.Command().handle()

        productoSeeder.Command().handle()

        userSeeder.Command().handle()

