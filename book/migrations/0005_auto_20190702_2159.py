# Generated by Django 2.2.3 on 2019-07-03 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20190702_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentbook',
            name='delivery_date_forecast',
            field=models.DateField(blank=True),
        ),
    ]