from django.db import models
import datetime

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adress = models.CharField(max_length=200)
    registration_date = models.DateField()

    def __str__(self):
        return f'Client_name: {self.name}, phone: {self.phone_number}, adress: {self.adress}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    value = models.IntegerField()
    date_add = models.DateField()
    data = models.FileField(upload_to='Homework_4', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
