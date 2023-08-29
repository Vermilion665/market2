from django import forms
from .models import *
# import datetime
# from my_project.settings import DATE_INPUT_FORMATS


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'slug': 'URL-адрес',
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'
        labels = {
            'name': 'Подкатегория',
            'category': 'Категория',
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['created_at', 'is_available']


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'


# class EmployeeForm(forms.ModelForm):
#     birthday = forms.DateField(input_formats=DATE_INPUT_FORMATS, label='Дата рождения',
#                                widget=forms.DateInput(attrs={'type': 'date'}))
#     class Meta:
#         model = Employee
#         fields = '__all__'
