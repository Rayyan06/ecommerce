# Generated by Django 3.1.5 on 2021-01-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210107_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, to='auctions.Listing'),
        ),
    ]