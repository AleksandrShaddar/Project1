from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.


@admin.action(description='Обновить адрес')
def update_adress(modeladmin, request, queryset):
    queryset.update(adress='Новый адрес')


@admin.action(description='Установить количество 0')
def update_value(modeladmin, request, queryset):
    queryset.update(value=0)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_ordered']
    list_per_page = 10
    search_fields = ['id']
    fieldsets = [
        (
            'Клиент',
            {
                'fields': ['customer'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Содержимое заказа',
                'fields': ['products'],
            },
        ),
        (
            'Стоимость заказа',
            {
                'fields': ['total_price']
            }
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'value']
    ordering = ['-date_add']
    list_per_page = 10
    search_fields = ['name']
    actions = [update_value]
    fieldsets = [
        (
            'Товар',
            {
                'fields': [('name', 'date_add')],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Информация о продукте',
                'fields': ['description'],
            },
        ),
        (
            'Стоимость и остаток',
            {
                'fields': ['price', 'value'],
            }
        ),
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'adress']
    ordering = ['-registration_date']
    list_per_page = 10
    search_fields = ['phone_number']
    actions = [update_adress]
    fieldsets = [
        (
            'Клиент',
            {
                'fields': [('name', 'phone_number')],
            },
        ),
        (
            'Подробности',
            {
                'description': 'Адрес клиента',
                'fields': ['adress'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'fields': ['email'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дополнительная информация',
                'fields': ['registration_date'],
            }
        ),
    ]
