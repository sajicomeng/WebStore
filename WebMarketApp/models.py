from django.db import models

class Customer(models.Model):

    username = models.CharField(max_length = 50, unique=True)
    mail = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()


class Meta:
    db_table = "customer"
# Create your models here.
