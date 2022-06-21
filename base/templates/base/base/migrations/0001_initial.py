# Generated by Django 3.0.5 on 2022-05-31 10:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('phone_num', models.CharField(max_length=10)),
                ('img', models.ImageField(null=True, upload_to='static/images/')),
                ('gender', models.CharField(choices=[('Other', 'Other'), ('Female', 'Female'), ('Male', 'Male')], default='Other', max_length=10)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(choices=[('GAUTENG', 'GAUTENG'), ('LIMPOPO', 'LIMPOPO'), ('DURBAN', 'DURBAN'), ('CAPE TOWN', 'CAPE TOWN'), ('MPUMALANGA', 'MPUMALANGA')], default='Other', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_num', models.CharField(max_length=10)),
                ('location', models.CharField(choices=[('GAUTENG', 'GAUTENG'), ('LIMPOPO', 'LIMPOPO'), ('DURBAN', 'DURBAN'), ('CAPE TOWN', 'CAPE TOWN'), ('MPUMALANGA', 'MPUMALANGA')], default='GAUTENG', max_length=50)),
                ('img', models.ImageField(null=True, upload_to='static/images/')),
                ('qualification', models.CharField(max_length=500)),
                ('subject', models.CharField(choices=[('Mathematics', 'Mathematics'), ('Physical Science', 'Physical Science'), ('English', 'English'), ('Accounting', 'Accounting'), ('Information Technology', 'Information Technology'), ('Chemistry', 'Chemistry'), ('Economics', 'Economics'), ('Programming', 'Programming'), ('Engineering', 'Engineering'), ('Bussiness', 'Business'), ('Geography', 'Geography'), ('History', 'History'), ('Statistics', 'Statistics'), ('Marketing', 'Marketing'), ('Law', 'Law')], default='Other', max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('fee_field', models.DecimalField(decimal_places=2, default=250.0, max_digits=6)),
                ('Experiance', models.CharField(default='', max_length=1200)),
                ('gender', models.CharField(choices=[('Other', 'Other'), ('Female', 'Female'), ('Male', 'Male')], default='Other', max_length=10)),
                ('tutoring_location', models.CharField(choices=[('ONLINE', 'ONLINE'), ('CONTACT', 'CONTACT'), ('HYBRID', 'HYBRID')], default='HYBRID', max_length=50)),
                ('serv_desc', models.CharField(default='', max_length=1200)),
                ('facebook_link', models.CharField(default='', max_length=100)),
                ('instagram_link', models.CharField(default='', max_length=100)),
                ('linkedin_link', models.CharField(default='', max_length=100)),
            ],
        ),
    ]