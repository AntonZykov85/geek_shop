from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.db import connection
from django.db.models import Q

class Command(BaseCommand):
   def handle(self, *args, **options):
       test_products = Product.objects.filter(
           # Q(category__name='Аксессуары') | Q(id=4)
           ~Q(category__name='Аксессуары') | Q(id=4)
       )

       print(test_products)
       # print(test_products)

