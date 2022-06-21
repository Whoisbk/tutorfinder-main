from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from .models import User,Students,Tutors
from django.contrib.auth.forms import UserCreationForm
LEVEL_CHOICES  = (
    ("Any","Any"),
    ("Primary","Primary"),
    ("Secondary","Secondary"),
    ("Tetiary","Tetiary"),
)
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

SUBJECT_CHOICES  = (
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
TUTORING_CHOICES  = (
    ("------","------"),
    ("ONLINE","ONLINE"),
    ("CONTACT","CONTACT"),
    ("HYBRID","HYBRID"),
)
PRICE_RANGE = (
    ("Under R50","Under R50"),
    ("R50 to R100","R50 to R100"),
    ("R100 to R150","R100 to R150"),
    ("R150 to R200","R150 to R200"),
    ("R200 & Above","R200 & Above"),
)
class SigninUser(forms.Form):
    username = forms.EmailField(required=False,max_length=200,label="",widget=forms.EmailInput(
        attrs={'class':'email-input',
        'title':'name',
        }))
    pass1 = forms.CharField(required=False,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'password-input',
        }))

class CreateTutor(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'username-input',
        }))
    id_num = forms.CharField(widget=forms.NumberInput(
        attrs={'class':'username-input',
        }))
    fname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'fname-input',
        }))
    lname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'lname-input',
        }))
    phone = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'phone-input',
        }))
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(
        attrs={'class':'phone-input',
        }))
    pass1 = forms.CharField(required=True,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'pass-input',
       }))
    pass2 = forms.CharField(required=True,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'pass-input',
        }))

    img_field = forms.ImageField(required=False)
    
    fee = forms.DecimalField(required=False,max_digits=5,decimal_places=2,label="",widget=forms.NumberInput(
        attrs={'class':'fee-input',}))
    price_range = forms.ChoiceField(required=False,choices = PRICE_RANGE,label ="",widget=forms.Select(
        attrs={'class':'prov-input'}))
    experiance = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
        attrs={'size':'80',
        'placeholder':'Enter your Experiances(Optional)'}))
    qualification = forms.CharField(required=False,max_length=1200,label="",widget=forms.Textarea(
        attrs={
        'placeholder':'Enter your Qualifications(Optional)'}))
    service_desc = forms.CharField(required=False,max_length=1200,label="",widget=forms.Textarea(
        attrs={'size':'80',
        'placeholder':'Description of your services(Optional)'}))

    tut_loc = forms.ChoiceField(required=False,choices = TUTORING_CHOICES,label ="",widget=forms.Select(
        attrs={'class':'prov-input'}))
    
    location = forms.ChoiceField(required=False,choices = PROVINCE_CHOICES,widget=forms.Select(
        attrs={'class':'prov-input'}))

    linkedin_link = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'email-input'
        }))
    facebook_link = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'email-input'
        }))
    instagram_link = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'email-input'
        }))
    
    class Meta:
        model = User
        fields = ('is_Tutor',)

class Send_Email(forms.Form):
    fname = forms.CharField(required=False,max_length=200,label="Enter Your Name",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="Enter Your Last Name",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Last Name'}))
    
    from_email = forms.EmailField(required=False,max_length=200,label="Enter Your Email",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Senders Email'}))
    to_email = forms.EmailField(required=False,max_length=200,label="Enter Tutors Email",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Recipient Email'}))
    service_focus = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
        attrs={'size':'40',
        'class':'form-control',
        'placeholder':'specify to the tutor what you want to focus on in these subjects'}))
    
class Send_Student_Email(forms.Form):
    fname = forms.CharField(required=False,max_length=200,label="Enter Your Name",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'First Name'}))

    lname = forms.CharField(required=False,max_length=200,label="Enter your LastName",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Last Name'}))
    
    from_email = forms.EmailField(required=False,max_length=200,label="Tutor Email",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Tutors Email'}))
    to_email1 = forms.EmailField(required=False,max_length=200,label="Student Email",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email2 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email3 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email4 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email5 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email6 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email7 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email8 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email9 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email10 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email11 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email12 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email13 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email14 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email15 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    date = forms.DateField(required=False,label="",widget=forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'size':'50',
        'class':'form-control',
        'type':'date'}))
    ms_teams_link = forms.URLField(required=False,max_length=200,label="Microsoft Teams Link")
    Time = forms.TimeField(required=False,label="Time of Meeting",widget=forms.TimeInput(
        attrs={'format':'%H:%M',
        'class':'form-control',
        'type':'time'}))
    service_focus = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
        attrs={'size':'80',
        'class':'form-control',
        'placeholder':'Meeting Details'}))
  
class CreateStud(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'username-input',
        }))
    id_num = forms.CharField(widget=forms.NumberInput(
        attrs={'class':'username-input',
        }))
    fname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'fname-input',
        }))
    lname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'lname-input',
        }))
    phone = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'phone-input',
        }))
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(
        attrs={'class':'phone-input',
        }))
    pass1 = forms.CharField(required=True,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'pass-input',
       }))
    pass2 = forms.CharField(required=True,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'pass-input',
        }))
    
    img_field = forms.ImageField(required=False,)

    phone = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'phone-input',
        }))
    
    location = forms.ChoiceField(required=False,choices = PROVINCE_CHOICES,widget=forms.Select(
        attrs={'class':'prov-input'}))

    class Meta:
        model = User
        fields = ('is_Student',)
    
class EditUser(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Username'}))
    fname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Last Name'}))
    
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.EmailInput(
        attrs={'size':'50',
        'placeholder':'Email'}))
        
    phone = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Phone Number'}))
    img_field = forms.ImageField(required=False)

class editTutor(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'username-input',
        'placeholder':'Username'
        }))
    fname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'fname-input','placeholder':'First Name'
        }))
    lname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'lname-input','placeholder':'Last Name'
        }))
    phone = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'phone-input','placeholder':'Phone'
        }))
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'email-input','placeholder':'Email'
        }))

    location = forms.ChoiceField(required = False,choices = PROVINCE_CHOICES)
   
    img_field = forms.ImageField(required=False)
    
    fee = forms.DecimalField(required=False,max_digits=6,label="",widget=forms.NumberInput(
        attrs={'class':'pass-input','placeholder':'Fee'}))
        
    qualification = forms.CharField(required=False,max_length=500,label="",widget=forms.Textarea(
        attrs={'class':'quali-input','placeholder':'Qualification'
        }))
    experiance = forms.CharField(required=False,max_length=500,label="",widget=forms.Textarea(
    attrs={'size':'80',
    'placeholder':'Experiance'}))

    service_desc = forms.CharField(required=False,max_length=500,label="",widget=forms.Textarea(
        attrs={'size':'80',
        'placeholder':'Description of your services'}))

    
    linkedin_link = forms.CharField(required=False,max_length=200,label="Linked-in link",widget=forms.TextInput(
        attrs={'class':'email-input'
        }))
    facebook_link = forms.CharField(required=False,max_length=200,label="Facebook-link",widget=forms.TextInput(
        attrs={'class':'email-input'
        }))
    instagram_link = forms.CharField(required=False,max_length=200,label="Instagram-link",widget=forms.TextInput(
        attrs={'class':'email-input'
        }))
    tut_loc = forms.ChoiceField(required = False,choices = TUTORING_CHOICES,label ="Tutoring Type")
    
class SubjectForm(forms.Form): 
    subject = forms.MultipleChoiceField(required=False,choices = SUBJECT_CHOICES,widget=forms.CheckboxSelectMultiple)
    level = forms.ChoiceField(required = False,choices = LEVEL_CHOICES)

class Reject_Email(forms.Form):
    fname = forms.CharField(required=False,max_length=200,label="Enter Your Name",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="Enter Your Last Name",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Last Name'}))
    
    from_email = forms.EmailField(required=False,max_length=200,label="Enter Your Email",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Senders Email'}))
    to_email1 = forms.EmailField(required=False,max_length=200,label="Student Email",widget=forms.TextInput(
        attrs={'size':'20',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email2 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email3 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email4 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email5 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email6 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email7 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email8 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email9 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email10 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email11 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email12 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email13 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email14 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
    to_email15 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'class':'form-control',
        'placeholder':'Student Email'}))
 
class DeleteUser(forms.Form):
    class Meta:
        model = User
        fields = []