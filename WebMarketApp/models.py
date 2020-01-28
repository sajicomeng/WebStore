from django.db import models

class Customer(models.Model):

    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    username = models.CharField(max_length = 50, unique=True)
    mail = models.CharField(max_length = 50, default='info@python.com')
    password = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()


class Meta:
    db_table = "customer"
# Create your models here.
