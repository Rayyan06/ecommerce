# Generated by Django 3.1.5 on 2021-01-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20210108_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('FA', 'Fashion'), ('TO', 'Toys'), ('EL', 'Electronics'), ('HO', 'Home'), ('EN', 'Entertainment'), ('CA', 'Cars')], max_length=2),
        ),
    ]
