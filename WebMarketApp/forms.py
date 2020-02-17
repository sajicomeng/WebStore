from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.db import models
from .models import Customer
from django import forms

class CustomerForm(ModelForm):
    password2 = forms.CharField(max_length=50)
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'phonenumber', 'mail', 'username', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
    def password_match(self):
        print(self.data['password2'])
        if self.Meta.model.password == self.data['password2']:
            return True
        return False

    def password_haslower(self):
        if any(c.islower() for c in self.Meta.model.password):
            return True
        return False

    def is_valid(self):
        if self.password_match():
            return True
        return False

    def clean(self):
        cleaned_data = super().clean()  # call the super clean() method first

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password2')

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Password error")


