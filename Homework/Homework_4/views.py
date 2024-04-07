from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from Homework_2.models import Product
from Homework_4.forms import ProductForm


# Create your views here.

def update_product(request):
    message = 'Укажите ID товара и новые данные о нем'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            id_ = form.cleaned_data['id_']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            value = form.cleaned_data['value']
            date_add = form.cleaned_data['date_add']
            image = form.cleaned_data['image']
            # fs = FileSystemStorage()
            product = Product.objects.filter(id=id_).first()
            if product is not None:
                if image is not None:
                    product.data = image
                    # fs.save(image.name, image)
                product.name = name
                product.description = description
                product.price = price
                product.value = value
                product.date_add = date_add
                product.save()
                message = 'Товар успешно изменен'
            else:
                message = f'Товара с Id={id_} не найдено'
    else:
        form = ProductForm()
    return render(request, 'Homework_4/update_product.html', {'form': form, 'message': message})
