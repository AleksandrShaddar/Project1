from django.core.management.base import BaseCommand
from Homework_2.models import Client, Product, Order
from random import randint, random
from datetime import date


class Command(BaseCommand):
    help = "Generate fake clients and products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru', phone_number=randint(100, 200), adress=f'City{i}', registration_date=date.today())
            client.save()
            product = Product(name=f'Product{i}', description=f'Description{i}', price=(random() + randint(10, 1000)), value=randint(1, 25), date_add=date.today())
            product.save()
            for j in range(1, count + 1):
                order = Order(customer=client, total_price=f'{product.price}')
                order.save()
