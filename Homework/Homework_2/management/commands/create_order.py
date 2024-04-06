from django.core.management.base import BaseCommand
from Homework_2.models import Client, Product, Order
from random import randint

class Command(BaseCommand):
    help = "Generate fake order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(id=pk).first()
        products = []
        common_price = 0
        if client is not None:
            for i in range(3):
                item = Product.objects.filter(id=(randint(15, 24))).first()
                common_price += item.price
                products.append(item)
        new_order = Order(customer=client, total_price=common_price)
        new_order.save()
        for elem in products:
            new_order.products.add(elem)
        print(products, common_price)
            # new_order = Order(customer=client, )
            # new_order =

            #     common_price = 0

        #     print(client, common_price)
        #     order = Order(customer=client, products=order.products_set.set([products]), total_price=common_price)
        #     order.save()
        # order = Order(customer=client, products=products, total_price=common_price)
        # order.customer.add(client)
        # order.products.add(products)


