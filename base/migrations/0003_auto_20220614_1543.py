# Generated by Django 3.0.5 on 2022-06-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220614_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutors',
            name='fee_field',
            field=models.DecimalField(decimal_places=2, default=250.0, max_digits=5),
        ),
    ]
