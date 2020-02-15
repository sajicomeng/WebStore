from django.forms import ModelForm
from django.db import models
from .models import Customer
from django import forms

class CustomerForm(ModelForm):
    password2 = models.CharField(max_length=50, default='')
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

