# Generated by Django 2.2.3 on 2019-07-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_copybook_edition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copybook',
            name='edition',
            field=models.IntegerField(blank=True),
        ),
    ]