from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Заполняет базу тестовыми данными"

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "categories")
        call_command("loaddata", "products")

        self.stdout.write(self.style.SUCCESS("База данных заполнена"))
