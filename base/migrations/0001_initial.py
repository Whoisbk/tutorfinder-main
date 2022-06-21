# Generated by Django 3.0.5 on 2022-06-21 20:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_Tutor', models.BooleanField(default=False)),
                ('is_Student', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_id_num', models.CharField(default=0, max_length=13)),
                ('user_dob', models.CharField(default='none', max_length=13)),
                ('user_age', models.CharField(default='none', max_length=3)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_num', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('img', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('gender', models.CharField(default='Other', max_length=10)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(choices=[('Other', 'Other'), ('Tshwane', (('Akasia', 'Akasia'), ('Atteridgeville', 'Atteridgeville'), ('Bronkhorstspruit', 'Bronkhorstspruit'), ('Centurion', 'Centurion'), ('Ga-Rankuwa', 'Ga-Rankuwa'), ('Hammanskraal', 'Hammanskraal'), (' Mabopane', ' Mabopane'), ('Mamelodi', ' Mamelodi'), ('Pretoria', 'Pretoria'), ('Pretoria', 'Pretoria'), ('Soshanguve', 'Soshanguve'), ('Temba', 'Temba'))), ('Johannesburg', (('Alexandra', 'Alexandra'), ('Diepkloof', 'Diepkloof'), ('Diepsloot', 'Diepsloot'), ('Johannesburg', 'Johannesburg'), ('Midrand', 'Midrand'), ('Randburg', 'Randburg'), (' Roodepoort', ' Roodepoort'), ('Sandton', ' Sandton'), ('Soweto', 'Soweto'))), ('Limpopo', (('Modimolle', 'Modimolle'), ('Mookgophong (Naboomspruit)', 'Mookgophong (Naboomspruit)'), ('Vaalwater', 'Vaalwater'), ('Bela-Bela', 'Bela-Bela'), ('Polokwane', 'Polokwane'))), ('KZN', (('Dannhauser', 'Dannhauser'), ('Hattingspruit', 'Hattingspruit'))), ('Mpumalanga', (('Amsterdam', 'Amsterdam'), ('Standerton', 'Standerton'), ('Lydenburg', 'Lydenburg'), ('Mashishing', 'Mashishing'), ('Sabie', 'Sabie'), ('eMkhondo (Piet Retief)', 'eMkhondo (Piet Retief)'))), ('Eastern Cape', (('Hofmeyr', 'Hofmeyr'), ('Molteno', 'Molteno'), ('Sterkstroom', 'Sterkstroom'), ('Tarkastad', 'Tarkastad'))), ('Free State', (('Hobhouse', 'Hobhouse'), ('Ladybrand', 'Ladybrand'), ('Tweespruit', 'Tweespruit'), ('Clocolan', 'Clocolan'), ('Marquard', 'Marquard'), ('Marquard', 'Marquard'))), ('Northern Cape', (('Garies', 'Garies'), ('Hondeklip Bay', 'Hondeklip Bay'), ('Kamieskroon', 'Kamieskroon'), ('Koingnaas', 'Koingnaas'), ('Leliefontein/Kamiesberg', 'Leliefontein/Kamiesberg'))), ('North West', (('Derby', 'Derby'), ('Koster', 'Koster'), ('Swartruggens', 'Swartruggens'))), ('Western Cape', (('Albertinia', 'Albertinia'), ('Gouritsmond', 'Gouritsmond'), ('Heidelberg', 'Heidelberg'), ('Jongensfontein', 'Jongensfontein'), ('Riversdale', 'Riversdale'), ('Slangrivier', 'Slangrivier'), ('Still Bay', 'Still Bay')))], default='Other', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_num', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('location', models.CharField(choices=[('Other', 'Other'), ('Tshwane', (('Akasia', 'Akasia'), ('Atteridgeville', 'Atteridgeville'), ('Bronkhorstspruit', 'Bronkhorstspruit'), ('Centurion', 'Centurion'), ('Ga-Rankuwa', 'Ga-Rankuwa'), ('Hammanskraal', 'Hammanskraal'), (' Mabopane', ' Mabopane'), ('Mamelodi', ' Mamelodi'), ('Pretoria', 'Pretoria'), ('Pretoria', 'Pretoria'), ('Soshanguve', 'Soshanguve'), ('Temba', 'Temba'))), ('Johannesburg', (('Alexandra', 'Alexandra'), ('Diepkloof', 'Diepkloof'), ('Diepsloot', 'Diepsloot'), ('Johannesburg', 'Johannesburg'), ('Midrand', 'Midrand'), ('Randburg', 'Randburg'), (' Roodepoort', ' Roodepoort'), ('Sandton', ' Sandton'), ('Soweto', 'Soweto'))), ('Limpopo', (('Modimolle', 'Modimolle'), ('Mookgophong (Naboomspruit)', 'Mookgophong (Naboomspruit)'), ('Vaalwater', 'Vaalwater'), ('Bela-Bela', 'Bela-Bela'), ('Polokwane', 'Polokwane'))), ('KZN', (('Dannhauser', 'Dannhauser'), ('Hattingspruit', 'Hattingspruit'))), ('Mpumalanga', (('Amsterdam', 'Amsterdam'), ('Standerton', 'Standerton'), ('Lydenburg', 'Lydenburg'), ('Mashishing', 'Mashishing'), ('Sabie', 'Sabie'), ('eMkhondo (Piet Retief)', 'eMkhondo (Piet Retief)'))), ('Eastern Cape', (('Hofmeyr', 'Hofmeyr'), ('Molteno', 'Molteno'), ('Sterkstroom', 'Sterkstroom'), ('Tarkastad', 'Tarkastad'))), ('Free State', (('Hobhouse', 'Hobhouse'), ('Ladybrand', 'Ladybrand'), ('Tweespruit', 'Tweespruit'), ('Clocolan', 'Clocolan'), ('Marquard', 'Marquard'), ('Marquard', 'Marquard'))), ('Northern Cape', (('Garies', 'Garies'), ('Hondeklip Bay', 'Hondeklip Bay'), ('Kamieskroon', 'Kamieskroon'), ('Koingnaas', 'Koingnaas'), ('Leliefontein/Kamiesberg', 'Leliefontein/Kamiesberg'))), ('North West', (('Derby', 'Derby'), ('Koster', 'Koster'), ('Swartruggens', 'Swartruggens'))), ('Western Cape', (('Albertinia', 'Albertinia'), ('Gouritsmond', 'Gouritsmond'), ('Heidelberg', 'Heidelberg'), ('Jongensfontein', 'Jongensfontein'), ('Riversdale', 'Riversdale'), ('Slangrivier', 'Slangrivier'), ('Still Bay', 'Still Bay')))], default='GAUTENG', max_length=50)),
                ('img', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('qualification', models.CharField(default='Under Contruction', max_length=500)),
                ('subject', multiselectfield.db.fields.MultiSelectField(choices=[('Accounting', 'Accounting'), ('Agricultural Sciences', 'Agricultural Sciences'), ('Algebra', 'Algebra'), ('Anatomy', 'Anatomy'), ('Biochemistry', 'Biochemistry'), ('Biblical Studies', 'Biblical Studies'), ('Biology', 'Biology'), ('Business Law', 'Business Law'), ('Business Studies', 'Business Studies'), ('Criminology', 'Criminology'), ('Calculus', 'Calculus'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Creative Writing', 'Creative Writing'), ('Computer Literacy', 'Computer Literacy'), ('Consumer Studies', 'Consumer Studies'), ('Design n Technology', 'Design n Technology'), ('Drama', 'Drama'), ('Economics', 'Economics'), ('English', 'English'), ('English Home Language', 'English Home Language'), ('English FAL', 'English FAL'), ('English Literature', 'English Literature'), ('Engineering', 'Engineering'), ('Engineering Graphics and Design', 'Engineering Graphics and Design'), ('Essay Writing', 'Essay Writing'), ('Finance', 'Finance'), ('Geography', 'Geography'), ('Geometry', 'Geometry'), ('Graphic Design', 'Graphic Design'), ('History', 'History'), ('Information Technology', 'Information Technology'), ('Human Biology', 'Human Biology'), ('Humanities', 'Humanities'), ('Journalism', 'Journalism'), ('Law', 'Law'), ('Legal Studies', 'Legal Studies'), ('Life Sciences', 'Life Sciences'), ('Mathematics', 'Mathematics'), ('Mathematical Literacy', 'Mathematical Literacy'), ('Medicine', 'Medicine'), ('Music', 'Music'), ('Nursing', 'Nursing'), ('Physical Science', 'Physical Science'), ('Programming', 'Programming'), ('Physiology', 'Physiology'), ('Statistics', 'Statistics'), ('Religion studies', 'Religion studies'), ('Visual Arts', 'Visual Arts')], default='Other', max_length=649)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('fee_field', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('Experiance', models.CharField(default='Under Contruction', max_length=1200)),
                ('gender', models.CharField(default='Other', max_length=10)),
                ('tutoring_location', models.CharField(choices=[('ONLINE', 'ONLINE'), ('CONTACT', 'CONTACT'), ('HYBRID', 'HYBRID')], default='HYBRID', max_length=50)),
                ('serv_desc', models.CharField(default='Under Contruction', max_length=1200)),
                ('facebook_link', models.CharField(default='', max_length=100)),
                ('instagram_link', models.CharField(default='', max_length=100)),
                ('linkedin_link', models.CharField(default='', max_length=100)),
                ('level', models.CharField(choices=[('Any', 'Any'), ('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Tetiary', 'Tetiary')], default='Any', max_length=10)),
                ('price_range', models.CharField(choices=[('Under R50', 'Under R50'), ('R50 to R100', 'R50 to R100'), ('R100 to R150', 'R100 to R150'), ('R150 to R200', 'R150 to R200'), ('R200 & Above', 'R200 & Above')], default='-----', max_length=50)),
            ],
        ),
    ]
