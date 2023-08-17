from django import forms
from django.forms import ModelForm
from .models import *
import datetime
from my_project.settings import DATE_INPUT_FORMATS


def year_choices():
    return [(r, r) for r in range(1950, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year



class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

 

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['age']

    birthday = forms.DateField(input_formats=DATE_INPUT_FORMATS, label='Дата рождения',
                               widget=forms.DateInput(attrs={'type': 'date'}))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=DATE_INPUT_FORMATS, label='Дата рождения',
                               widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Employee
        fields = '__all__'
