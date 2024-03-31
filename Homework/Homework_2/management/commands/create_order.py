from django.core.management.base import BaseCommand
from Homework_2.models import Client, Product, Order
from random import randint

class Command(BaseCommand):
    help = "Generate fake order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            products = []
            common_price = 0
            for i in range(3):
                item = Product.objects.filter(pk=randint(1, 6)).first()
                common_price += item.price
                products.append(item)
            print(client, common_price)
            order = Order(customer=client, products=order.products_set.set([products]), total_price=common_price)
            order.save()
            # order = Order(customer=client, products=products, total_price=common_price)
            # order.customer.add(client)
            # order.products.add(products)
            

