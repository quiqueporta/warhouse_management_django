# Generated by Django 2.0.1 on 2018-05-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_management', '0002_auto_20180514_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseitemmapper',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
