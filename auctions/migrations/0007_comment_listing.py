# Generated by Django 3.1.5 on 2021-01-08 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210107_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing'),
            preserve_default=False,
        ),
    ]