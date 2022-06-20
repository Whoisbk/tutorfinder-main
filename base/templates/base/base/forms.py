from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from .models import User,Students,Tutors
from django.contrib.auth.forms import UserCreationForm
 

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
TUTORING_CHOICES  = (
    ("------","------"),
    ("ONLINE","ONLINE"),
    ("CONTACT","CONTACT"),
    ("HYBRID","HYBRID"),
)

class SigninUser(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
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
    id_num = forms.CharField(widget=forms.TextInput(
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
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'email-input',
        }))
    pass1 = forms.CharField(required=True,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'pass-input',
       }))
    pass2 = forms.CharField(required=True,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'pass-input',
        }))

    subject = forms.MultipleChoiceField(required=False,choices = SUBJECT_CHOICES,widget=forms.CheckboxSelectMultiple
        )
    img_field = forms.ImageField(required=False)
    
    fee = forms.DecimalField(required=False,max_digits=6,label="",widget=forms.NumberInput(
        attrs={'class':'fee-input',}))
    
    experiance = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
        attrs={'size':'80'}))
    qualification = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'quali-input',
        }))
    service_desc = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
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
        attrs={'size':'50',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="Enter Your Last Name",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Last Name'}))
    
    from_email = forms.EmailField(required=False,max_length=200,label="Enter Your Email",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Senders Email'}))
    to_email = forms.EmailField(required=False,max_length=200,label="Enter Tutors Email",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Recipient Email'}))
    subject = forms.MultipleChoiceField(required=False,choices = SUBJECT_CHOICES,widget=forms.CheckboxSelectMultiple
        )
    service_focus = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
        attrs={'size':'80',
        'placeholder':'specify to the tutor what you want to focus on in these subjects'}))
    
class Send_Student_Email(forms.Form):
    fname = forms.CharField(required=False,max_length=200,label="Enter Your Name",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="Enter your LastName",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Last Name'}))
    
    from_email = forms.EmailField(required=False,max_length=200,label="Tutor Email",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Tutors Email'}))
    to_email1 = forms.EmailField(required=False,max_length=200,label="Student Email",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email2 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email3 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email4 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email5 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email6 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email7 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email8 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email9 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email10 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email11 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email12 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email13 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email14 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    to_email15 = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Student Email'}))
    subject = forms.MultipleChoiceField(required=False,choices = SUBJECT_CHOICES,widget=forms.CheckboxSelectMultiple
        )
    ms_teams_link = forms.URLField(required=False,max_length=200,label="Microsoft Teams Link")
    
    service_focus = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
        attrs={'size':'80',
        'placeholder':'Meeting Details'}))
  

class CreateStud(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'username-input',
        }))
    id_num = forms.CharField(widget=forms.TextInput(
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
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'email-input',
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
    
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Email'}))
    phone = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Phone Number'}))


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

    qualification = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'quali-input','placeholder':'Qualification'
        }))
   
    img_field = forms.ImageField(required=False)
    
    fee = forms.DecimalField(required=False,max_digits=6,label="",widget=forms.NumberInput(
        attrs={'class':'pass-input','placeholder':'Fee'}))
    
    experiance = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
    attrs={'size':'80',
    'placeholder':'Experiance'}))

    service_desc = forms.CharField(required=False,max_length=200,label="",widget=forms.Textarea(
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
    subject = forms.MultipleChoiceField(required=False,choices = SUBJECT_CHOICES,widget=forms.CheckboxSelectMultiple
        )

    
class DeleteUser(forms.Form):
    class Meta:
        model = User
        fields = []