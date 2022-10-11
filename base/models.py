from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from multiselectfield import MultiSelectField
from phone_field import PhoneField

# Create your models here.

PROVINCE_CHOICES  = [
    ("Other","Other"),
    ("Tshwane",(("Akasia","Akasia"),("Atteridgeville","Atteridgeville"),
    ("Bronkhorstspruit","Bronkhorstspruit"), ("Centurion","Centurion"),
    ("Ga-Rankuwa","Ga-Rankuwa"),("Hammanskraal","Hammanskraal"),(" Mabopane"," Mabopane"),
    ("Mamelodi"," Mamelodi"),("Pretoria","Pretoria"),("Pretoria","Pretoria"),
    ("Soshanguve","Soshanguve"),("Temba","Temba"),
    )),
    ("Johannesburg",(("Alexandra","Alexandra"),("Diepkloof","Diepkloof"),
    ("Diepsloot","Diepsloot"), ("Johannesburg","Johannesburg"),
    ("Midrand","Midrand"),("Randburg","Randburg"),(" Roodepoort"," Roodepoort"),
    ("Sandton"," Sandton"),("Soweto","Soweto"),
    )),
    ("Limpopo",(("Modimolle","Modimolle"),("Mookgophong (Naboomspruit)","Mookgophong (Naboomspruit)"),
    ("Vaalwater","Vaalwater"), ("Bela-Bela","Bela-Bela"),
    ("Polokwane","Polokwane"),
    )),
    ("KZN",(("Dannhauser","Dannhauser"),
    ("Hattingspruit","Hattingspruit"),
    )),
    ("Mpumalanga",(("Amsterdam","Amsterdam"),
    ("Standerton","Standerton"),("Lydenburg","Lydenburg"),
    ("Mashishing","Mashishing"),("Sabie","Sabie"),
    ("eMkhondo (Piet Retief)","eMkhondo (Piet Retief)"),
    )),
    ("Eastern Cape",(("Hofmeyr","Hofmeyr"),
    ("Molteno","Molteno"),("Sterkstroom","Sterkstroom"),
    ("Tarkastad","Tarkastad"),
    )),
    ("Free State",(("Hobhouse","Hobhouse"),
    ("Ladybrand","Ladybrand"),("Tweespruit","Tweespruit"),
    ("Clocolan","Clocolan"),("Marquard","Marquard"),
    ("Marquard","Marquard"),
    )),
    ("Northern Cape",(("Garies","Garies"),
    ("Hondeklip Bay","Hondeklip Bay"),("Kamieskroon","Kamieskroon"),
    ("Koingnaas","Koingnaas"),("Leliefontein/Kamiesberg","Leliefontein/Kamiesberg"),
    )),
    ("North West",(("Derby","Derby"),
    ("Koster","Koster"),("Swartruggens","Swartruggens"),
    )),
    ("Western Cape",(("Albertinia","Albertinia"),
    ("Gouritsmond","Gouritsmond"),("Heidelberg","Heidelberg"),
    ("Jongensfontein","Jongensfontein"),("Riversdale","Riversdale"),
    ("Slangrivier","Slangrivier"),("Still Bay","Still Bay"),
    )),
]
TUTORING_CHOICES  = (
    ("ONLINE","ONLINE"),
    ("CONTACT","CONTACT"),
    ("HYBRID","HYBRID"),
)
LEVEL_CHOICES  = (
    ("Any","Any"),
    ("Primary","Primary"),
    ("Secondary","Secondary"),
    ("Tetiary","Tetiary"),
)
PRICE_RANGE = (
    ("Under R50","Under R50"),
    ("R50 to R100","R50 to R100"),
    ("R100 to R150","R100 to R150"),
    ("R150 to R200","R150 to R200"),
    ("R200 & Above","R200 & Above"),
)

SUBJECT_CHOICES = (
    ("Accounting","Accounting"),
    ("Agricultural Sciences","Agricultural Sciences"),
    ("Algebra","Algebra"),
    ("Anatomy","Anatomy"),
    ("Biochemistry","Biochemistry"),
    ("Biblical Studies","Biblical Studies"),
    ("Biology","Biology"),
    ("Business Law","Business Law"),
    ("Business Studies","Business Studies"),
    ("Criminology","Criminology"),
    ("Calculus","Calculus"),
    ("Chemistry","Chemistry"),
    ("Computer Science","Computer Science"),
    ("Creative Writing","Creative Writing"),
    ("Computer Literacy","Computer Literacy"),
    ("Consumer Studies","Consumer Studies"),
    ("Design n Technology","Design n Technology"),
    ("Drama","Drama"),
    ("Economics","Economics"),
    ("English","English"),
    ("English Home Language","English Home Language"),
    ("English FAL","English FAL"),
    ("English Literature","English Literature"),
    ("Engineering","Engineering"),
    ("Engineering Graphics and Design","Engineering Graphics and Design"),
    ("Essay Writing","Essay Writing"),
    ("Finance","Finance"),
    ("Geography","Geography"),
    ("Geometry","Geometry"),
    ("Graphic Design","Graphic Design"),
    ("History","History"), 
    ("Information Technology","Information Technology"),
    ("Human Biology","Human Biology"),
    ("Humanities","Humanities"),
    ("Journalism","Journalism"),
    ("Law","Law"),
    ("Legal Studies","Legal Studies"),
    ("Life Sciences","Life Sciences"),
    ("Mathematics","Mathematics"),
    ("Mathematical Literacy","Mathematical Literacy"),
    ("Medicine","Medicine"),
    ("Music","Music"),
    ("Nursing","Nursing"),
    ("Physical Science","Physical Science"),
    ("Programming","Programming"),
    ("Physiology","Physiology"),
    ("Statistics","Statistics"),
    ("Religion studies","Religion studies"),
    ("Visual Arts","Visual Arts"),  
)

class User(AbstractUser):
    is_Tutor = models.BooleanField(default = False)
    is_Student = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    user_id_num = models.CharField(max_length = 13,default = 0)
    user_dob = models.CharField(max_length = 13,default = 'none')
    user_age = models.CharField(max_length = 3,default = 'none')
    def __str__(self):
        return str(self.first_name + " " + self.last_name)

'''
class Subject(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
    subject = MultiSelectField(choices = SUBJECT_CHOICES,default= "Other")
'''
class Tutors(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key = True)
    phone_num = PhoneField(blank= True)
    location = models.CharField(max_length = 50,choices= PROVINCE_CHOICES,default = "GAUTENG")
    img = models.ImageField(default = "default.png",null = True,blank = True) 
    qualification = models.CharField(max_length=500,default="Under Contruction" )
    subject = models.CharField(max_length = 600,choices=SUBJECT_CHOICES, default="Other")
    date_created = models.DateTimeField(default = timezone.now)
    fee_field = models.DecimalField(max_digits=5,decimal_places = 2,default=0)
    Experiance = models.CharField(max_length = 1200,default="Under Contruction")#add default exp 
    gender = models.CharField(max_length = 10,default = "Other")
    tutoring_location = models.CharField(max_length = 50,choices = TUTORING_CHOICES,default = "HYBRID")
    serv_desc = models.CharField(max_length = 1200,default="Under Contruction")
    facebook_link = models.CharField(max_length=100,default = "")
    instagram_link = models.CharField(max_length=100,default = "")
    linkedin_link = models.CharField(max_length=100,default = "")
    level = models.CharField(max_length = 10,choices = LEVEL_CHOICES,default = "Any")
    price_range = models.CharField(max_length = 50,choices = PRICE_RANGE,default = "-----")
    def __str__(self):
        return str(self.user.first_name)

class Students(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE ,primary_key = True)
    phone_num = PhoneField(blank= True)
    img = models.ImageField(default = "default.png",null = True,blank = True)
    gender = models.CharField(max_length = 10,default = "Other")
    date_created = models.DateTimeField(default = timezone.now)
    location = models.CharField(max_length = 50,choices= PROVINCE_CHOICES,default = "Other")

    def __str__(self):
        return str(self.user.first_name)