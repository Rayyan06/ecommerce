# Generated by Django 3.1.5 on 2021-01-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210107_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
