# Generated by Django 3.0.1 on 2019-12-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMarketApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
