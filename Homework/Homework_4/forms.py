from django import forms
import datetime


class ProductForm(forms.Form):
    id_ = forms.IntegerField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Описание товара'}
        ),
    )
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    value = forms.IntegerField()
    date_add = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
    )
    image = forms.ImageField(required=False)
