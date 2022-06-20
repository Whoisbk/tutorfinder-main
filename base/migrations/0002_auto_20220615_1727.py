# Generated by Django 3.0.5 on 2022-06-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='location',
            field=models.CharField(choices=[('Other', 'Other'), ('Tshwane', (('Akasia', 'Akasia'), ('Atteridgeville', 'Atteridgeville'), ('Bronkhorstspruit', 'Bronkhorstspruit'), ('Centurion', 'Centurion'), ('Ga-Rankuwa', 'Ga-Rankuwa'), ('Hammanskraal', 'Hammanskraal'), (' Mabopane', ' Mabopane'), ('Mamelodi', ' Mamelodi'), ('Pretoria', 'Pretoria'), ('Pretoria', 'Pretoria'), ('Soshanguve', 'Soshanguve'), ('Temba', 'Temba'))), ('Johannesburg', (('Alexandra', 'Alexandra'), ('Diepkloof', 'Diepkloof'), ('Diepsloot', 'Diepsloot'), ('Johannesburg', 'Johannesburg'), ('Midrand', 'Midrand'), ('Randburg', 'Randburg'), (' Roodepoort', ' Roodepoort'), ('Sandton', ' Sandton'), ('Soweto', 'Soweto'))), ('Limpopo', (('Modimolle', 'Modimolle'), ('Mookgophong (Naboomspruit)', 'Mookgophong (Naboomspruit)'), ('Vaalwater', 'Vaalwater'), ('Bela-Bela', 'Bela-Bela'), ('Polokwane', 'Polokwane'))), ('KZN', (('Dannhauser', 'Dannhauser'), ('Hattingspruit', 'Hattingspruit'))), ('Mpumalanga', (('Amsterdam', 'Amsterdam'), ('Standerton', 'Standerton'), ('Lydenburg', 'Lydenburg'), ('Mashishing', 'Mashishing'), ('Sabie', 'Sabie'), ('eMkhondo (Piet Retief)', 'eMkhondo (Piet Retief)'))), ('Eastern Cape', (('Hofmeyr', 'Hofmeyr'), ('Molteno', 'Molteno'), ('Sterkstroom', 'Sterkstroom'), ('Tarkastad', 'Tarkastad'))), ('Free State', (('Hobhouse', 'Hobhouse'), ('Ladybrand', 'Ladybrand'), ('Tweespruit', 'Tweespruit'), ('Clocolan', 'Clocolan'), ('Marquard', 'Marquard'), ('Marquard', 'Marquard'))), ('Northern Cape', (('Garies', 'Garies'), ('Hondeklip Bay', 'Hondeklip Bay'), ('Kamieskroon', 'Kamieskroon'), ('Koingnaas', 'Koingnaas'), ('Leliefontein/Kamiesberg', 'Leliefontein/Kamiesberg'))), ('North West', (('Derby', 'Derby'), ('Koster', 'Koster'), ('Swartruggens', 'Swartruggens'))), ('Western Cape', (('Albertinia', 'Albertinia'), ('Gouritsmond', 'Gouritsmond'), ('Heidelberg', 'Heidelberg'), ('Jongensfontein', 'Jongensfontein'), ('Riversdale', 'Riversdale'), ('Slangrivier', 'Slangrivier'), ('Still Bay', 'Still Bay')))], default='Other', max_length=50),
        ),
        migrations.AlterField(
            model_name='tutors',
            name='fee_field',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tutors',
            name='level',
            field=models.CharField(choices=[('Any', 'Any'), ('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Tetiary', 'Tetiary')], default='Any', max_length=10),
        ),
        migrations.AlterField(
            model_name='tutors',
            name='location',
            field=models.CharField(choices=[('Other', 'Other'), ('Tshwane', (('Akasia', 'Akasia'), ('Atteridgeville', 'Atteridgeville'), ('Bronkhorstspruit', 'Bronkhorstspruit'), ('Centurion', 'Centurion'), ('Ga-Rankuwa', 'Ga-Rankuwa'), ('Hammanskraal', 'Hammanskraal'), (' Mabopane', ' Mabopane'), ('Mamelodi', ' Mamelodi'), ('Pretoria', 'Pretoria'), ('Pretoria', 'Pretoria'), ('Soshanguve', 'Soshanguve'), ('Temba', 'Temba'))), ('Johannesburg', (('Alexandra', 'Alexandra'), ('Diepkloof', 'Diepkloof'), ('Diepsloot', 'Diepsloot'), ('Johannesburg', 'Johannesburg'), ('Midrand', 'Midrand'), ('Randburg', 'Randburg'), (' Roodepoort', ' Roodepoort'), ('Sandton', ' Sandton'), ('Soweto', 'Soweto'))), ('Limpopo', (('Modimolle', 'Modimolle'), ('Mookgophong (Naboomspruit)', 'Mookgophong (Naboomspruit)'), ('Vaalwater', 'Vaalwater'), ('Bela-Bela', 'Bela-Bela'), ('Polokwane', 'Polokwane'))), ('KZN', (('Dannhauser', 'Dannhauser'), ('Hattingspruit', 'Hattingspruit'))), ('Mpumalanga', (('Amsterdam', 'Amsterdam'), ('Standerton', 'Standerton'), ('Lydenburg', 'Lydenburg'), ('Mashishing', 'Mashishing'), ('Sabie', 'Sabie'), ('eMkhondo (Piet Retief)', 'eMkhondo (Piet Retief)'))), ('Eastern Cape', (('Hofmeyr', 'Hofmeyr'), ('Molteno', 'Molteno'), ('Sterkstroom', 'Sterkstroom'), ('Tarkastad', 'Tarkastad'))), ('Free State', (('Hobhouse', 'Hobhouse'), ('Ladybrand', 'Ladybrand'), ('Tweespruit', 'Tweespruit'), ('Clocolan', 'Clocolan'), ('Marquard', 'Marquard'), ('Marquard', 'Marquard'))), ('Northern Cape', (('Garies', 'Garies'), ('Hondeklip Bay', 'Hondeklip Bay'), ('Kamieskroon', 'Kamieskroon'), ('Koingnaas', 'Koingnaas'), ('Leliefontein/Kamiesberg', 'Leliefontein/Kamiesberg'))), ('North West', (('Derby', 'Derby'), ('Koster', 'Koster'), ('Swartruggens', 'Swartruggens'))), ('Western Cape', (('Albertinia', 'Albertinia'), ('Gouritsmond', 'Gouritsmond'), ('Heidelberg', 'Heidelberg'), ('Jongensfontein', 'Jongensfontein'), ('Riversdale', 'Riversdale'), ('Slangrivier', 'Slangrivier'), ('Still Bay', 'Still Bay')))], default='GAUTENG', max_length=50),
        ),
    ]
