from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from multiselectfield import MultiSelectField


# Create your models here.

PROVINCE_CHOICES  = (
    ("Other","Other"),
    ("GAUTENG,Soshanguve","GAUTENG,Soshanguve"),
    ("GAUTENG,Pretoria","GAUTENG,Pretoria"),
    ("GAUTENG,Centurion","GAUTENG,Centurion"),
    ("LIMPOPO,Bela Bela","LIMPOPO,Bela Bela"),
    ("LIMPOPO,Modimolle","LIMPOPO,Modimolle"),
    ("LIMPOPO,Polokwane","LIMPOPO,Polokwane"),
    ("CAPE TOWN","CAPE TOWN"),
    ("DURBAN","DURBAN"),
)

TUTORING_CHOICES  = (
    ("ONLINE","ONLINE"),
    ("CONTACT","CONTACT"),
    ("HYBRID","HYBRID"),
)

SUBJECT_CHOICES  = (
    ("Mathematics","Mathematics"),
    ("Physical Science","Physical Science"),
    ("English","English"),   
    ("Accounting","Accounting"),
    ("Information Technology","Information Technology"),
    ("Chemistry","Chemistry"),
    ("Economics","Economics"),
    ("Programming","Programming"),
    ("Engineering","Engineering"),
    ("Bussiness","Business"),
    ("Geography","Geography"),
    ("History","History"),
    ("Statistics","Statistics"),
    ("Marketing","Marketing"),
    ("Law","Law"),
)

class User(AbstractUser):
    is_Tutor = models.BooleanField(default = False)
    is_Student = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
    

class Tutors(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
    id_num = models.CharField(max_length = 13,default = 0)
    phone_num = models.CharField(max_length = 10)
    location = models.CharField(max_length = 50,choices= PROVINCE_CHOICES,default = "GAUTENG")
    img = models.ImageField(default = "default.png",null = True,blank = True)
    qualification = models.CharField(max_length=500)
    subject = MultiSelectField(choices = SUBJECT_CHOICES,default= "Other")
    date_created = models.DateTimeField(default = timezone.now)
    fee_field = models.DecimalField(max_digits=6,decimal_places = 2,default=250.00)
    Experiance = models.CharField(max_length = 1200,default="")#add default exp 
    gender = models.CharField(max_length = 10,default = "Other")
    tutoring_location = models.CharField(max_length = 50,choices = TUTORING_CHOICES,default = "HYBRID")
    serv_desc = models.CharField(max_length = 1200,default="")
    facebook_link = models.CharField(max_length=100,default = "")
    instagram_link = models.CharField(max_length=100,default = "")
    linkedin_link = models.CharField(max_length=100,default = "")

    
    def __str__(self):
        return str(self.user.first_name)

class Students(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE ,primary_key = True)
    id_num = models.CharField(max_length = 13,default = 0)
    phone_num = models.CharField(max_length = 10)
    img = models.ImageField(default = "default.png",null = True,blank = True)
    gender = models.CharField(max_length = 10,default = "Other")
    date_created = models.DateTimeField(default = timezone.now)
    location = models.CharField(max_length = 50,choices= PROVINCE_CHOICES,default = "Other")

    def __str__(self):
        return str(self.user.first_name)