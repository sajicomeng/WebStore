from django.db import models
from django import forms

class Customer(models.Model):

    firstname = models.CharField(verbose_name='First Name', max_length=50, default='', blank=True)
    lastname = models.CharField(verbose_name='Last Name', max_length=50, default='', blank=True)
    phonenumber = models.IntegerField(verbose_name = 'Phone Number', blank=True)
    mail = models.CharField(verbose_name='Email Addrees', max_length = 50, default='', blank=True)
    username = models.CharField(verbose_name='Username',  max_length = 50, unique=True)
    password = models.CharField(verbose_name='Password', max_length = 50, default='')


class Meta:
    db_table = "customer"
# Create your models here.
