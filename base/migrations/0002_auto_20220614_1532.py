# Generated by Django 3.0.5 on 2022-06-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutors',
            name='level',
            field=models.CharField(choices=[('Any', 'Any'), ('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Tetiary', 'Tetiary')], default='Any', max_length=10),
        ),
    ]
