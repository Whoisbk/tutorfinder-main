# Generated by Django 3.0.5 on 2022-06-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20220605_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='img',
            field=models.ImageField(blank=True, default='0x0.jpg', null=True, upload_to=''),
        ),
    ]
