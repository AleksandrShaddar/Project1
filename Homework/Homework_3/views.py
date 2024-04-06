from datetime import date, timedelta, datetime, timezone
from django.shortcuts import render
from Homework_2.models import Client, Order, Product


# Create your views here.

def order(request, pk):
    user = Client.objects.filter(id=pk).first()
    order = Order.objects.filter(customer=user).all()
    final_basket = {}
    for elem in range(len(order)):
        id_order = order[elem].id
        basket = Order.objects.filter(id=id_order)
        for item in basket.values('products'):
            for value in item.values():
                final_basket.setdefault(id_order, []).append(Product.objects.filter(id=value).first().name)
    context = {'user': user, 'value': len(order), 'order': order, 'final': final_basket}
    return render(request, 'Homework_3/orders.html', context)


def client_products(request, pk, dt):
    today = datetime.now(timezone.utc)
    some_day_before = today - timedelta(days=dt)
    user = Client.objects.filter(id=pk).first()
    order = Order.objects.filter(customer=user, date_ordered__gte=some_day_before)
    final_basket = []
    for elem in range(len(order)):
        id_order = order[elem].id
        basket = Order.objects.filter(id=id_order)
        for item in basket.values('products'):
            for value in item.values():
                if Product.objects.filter(id=value).first().name not in final_basket:
                    final_basket.append(Product.objects.filter(id=value).first().name)
    context = {'user': user, 'value': len(final_basket), 'order': order, 'final': final_basket, 'date': dt}
    return render(request, 'Homework_3/products.html', context)
