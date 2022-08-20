from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import SigninUser,CreateTutor,CreateStud,EditUser,DeleteUser,editTutor,UserCreationForm,Send_Email,Send_Student_Email,SubjectForm,Reject_Email
from .models import Tutors,Students,User
from django.contrib import messages
from .filters import TutorFilter 
from django.contrib import messages
from datetime import datetime
import decimal
from za_id_number.za_id_number import SouthAfricanIdentityValidate
from django.contrib.auth.signals import user_logged_in
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail #emailmessage class
from django.conf import settings #seetings to access the smtp config
from django.template.loader import render_to_string #send template as string to the email body and not html template
from bson.decimal128 import Decimal128
from django.core.paginator import Paginator
#add edit subject


# Create your views here.
@login_required(login_url ='signin')
def home(request): 

    tutDet = Tutors.objects.all()
    
    tutFilter = TutorFilter(request.GET,queryset = tutDet)
    tutcounter = tutFilter.qs.count()#count number of tutors found
    tutDet = tutFilter.qs #query all to tutors found from the searxh form
    #set up pagination
    p = Paginator(tutDet,3) 
    page = request.GET.get('page')
    tutor_list = p.get_page(page)

    context = {"tutor_list":tutor_list,"tutDet":tutDet,"tutFilter":tutFilter,"tutcounter":tutcounter}

    return render(request,"base/home.html",context)

def signin(request):
    if request.method == "POST":
        
        form = SigninUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            pass1 = form.cleaned_data["pass1"]
            try:
                if email == "":
                    messages.error(request,'Email is empty')
                    return redirect("signin")
                elif not User.objects.filter(email=email):
                    messages.error(request,'Create an Account')
                    return redirect("signin")
                elif pass1 == "":
                    messages.error(request,'Please enter password')
                    return redirect("signin")
                user = User.objects.get(email=email).username
                u = authenticate(username=user,password=pass1)
            except  Exception as e:
                messages.error(request,'Email is incorrect')
                return redirect("signin")
            if u is not None:
                login(request,u)
                return redirect("home")
            else:
                messages.error(request,'Password is Incorrect')
                return redirect("signin")
    else:
        form = SigninUser(request.POST)
    
    context = {"form": form}
    return render(request,"base/signin.html",context)

@login_required(login_url ='signin')
def display_subjects(request):
    return render(request,"base/display_subjects.html")


def success(request):
    return render(request,"base/success.html")

def instructions_stud(request):
    return render(request,"base/instructions_stud.html")


def instructions_tut(request):
    return render(request,"base/instructions_tut.html")

@login_required(login_url ='signin')
def how_it_works(request):
    return render(request,"base/how_it_works.html")

def subject_update(request):
    
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            request.session['subject'] = form.cleaned_data['subject']
            request.session['subject_2'] = request.POST.get('new_subject')
            request.session['level'] = form.cleaned_data['level']
            
            if request.session['subject'] == [] and request.session['subject_2'] is None:#if subject not chosen
                    messages.error(request,"Please Choose a subject before you continue")
                    form = SubjectForm(request.POST)
            else:
                return redirect('editTutorProfile')      
            
    else:
        form = SubjectForm(request.POST)
        
    context = {'form':form}

    return render(request,"base/subject_update.html",context)


def subject_choice_tut(request):
    
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            request.session['subject'] = form.cleaned_data['subject']
            request.session['subject_2'] = request.POST.get('new_subject')
            request.session['level'] = form.cleaned_data['level']
            print( request.session['subject'])
            print( request.session['subject_2'])
            if request.session['level'] == "Any" and request.session['subject'] == [] and request.session['subject_2'] is None:#if subject not chosen
                    messages.error(request,"Please Choose a subject before you continue")
                    form = SubjectForm(request.POST)
            else:
                return redirect('email_to_student')      
            
    else:
        form = SubjectForm(request.POST)
        
    context = {'form':form}

    return render(request,"base/subject_choice_tut.html",context)


def subject_choice_stud(request):
    
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            request.session['subject'] = form.cleaned_data['subject']
            request.session['subject_2'] = request.POST.get('new_subject')
            request.session['level'] = form.cleaned_data['level']
            print( request.session['subject'])
            print( request.session['subject_2'])
            if request.session['level'] == "Any" and request.session['subject'] == [] and request.session['subject_2'] is None:#if subject not chosen
                    messages.error(request,"Please Choose a subject before you continue")
                    form = SubjectForm(request.POST)
            else:
                return redirect('send_email')      
            
    else:
        form = SubjectForm(request.POST)
        
    context = {'form':form}

    return render(request,"base/subject_choice_stud.html",context)

def subject_choice(request):
    
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            request.session['subject'] = form.cleaned_data['subject']
            request.session['subject_2'] = request.POST.get('new_subject')
            request.session['level'] = form.cleaned_data['level']
            print( request.session['subject'])
            print( request.session['subject_2'])
            if request.session['level'] == "Any" and request.session['subject'] == [] and request.session['subject_2'] is None:#if subject not chosen
                    messages.error(request,"Please Choose a subject before you continue")
                    form = SubjectForm(request.POST)
            else:
                return redirect('RegTut')      
            
    else:
        form = SubjectForm(request.POST)
        
    context = {'form':form}

    return render(request,"base/subject_choice.html",context)

def RegTut(request):
    if request.method == "POST":
        form = CreateTutor(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            un = form.cleaned_data["username"]
            id_num = form.cleaned_data["id_num"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            e = form.cleaned_data["email"]
            p1 = form.cleaned_data["pass1"]
            p2 = form.cleaned_data["pass2"]
            phone = form.cleaned_data["phone"]
            locate = form.cleaned_data["location"]
            img= form.cleaned_data["img_field"]
            quali = form.cleaned_data["qualification"]
            subj = request.session["subject"]
            subj_2 = request.session["subject_2"]
            fee = form.cleaned_data["fee"]
            exp = form.cleaned_data["experiance"]
            tut_loc = form.cleaned_data["tut_loc"]
            service_desc = form.cleaned_data["service_desc"]
            facebook_link = form.cleaned_data["facebook_link"]
            instagram_link = form.cleaned_data["instagram_link"]
            linkedin_link = form.cleaned_data["linkedin_link"]
            level = request.session['level']
            price_range = form.cleaned_data['price_range']
            final_subj = ""
            
            if subj == []:
                final_subj = subj_2
            else: 
                final_subj = subj

            print(final_subj)
            
            idnum = "".join(str(id_num))

            za_id = SouthAfricanIdentityValidate(idnum)
            valid = za_id.validate()
            za_gender = za_id.get_gender()
            za_age = za_id.get_age()
            za_dob = za_id.calculate_birthday()

            print(valid)
            print(za_gender)
            print(za_age)
            print(za_dob)

            try:
                special_Sym = ["@","!","$","#"]
                if p1 != p2:#if passwords are not equal
                    messages.error(request,"Passwords are not equal")
                    form = CreateTutor(request.POST,request.FILES)
                elif fname=="":
                    messages.error(request,"Enter your name")
                    form = CreateTutor(request.POST,request.FILES)
                elif lname=="":
                    messages.error(request,"Enter your last name")
                    form = CreateTutor(request.POST,request.FILES)
                elif not valid:#if id is too short
                    messages.error(request,"Your ID is not valid")
                    form = CreateTutor(request.POST,request.FILES)
                elif len(id_num) != 13:#if id is too short
                    messages.error(request,"ID is not 13 numbers")
                    form = CreateTutor(request.POST,request.FILES)
                elif len(p1) <= 6:#if password is too short
                    messages.error(request,"Password is too short must be more than 6 characters")
                    form = CreateTutor(request.POST,request.FILES)
                elif idnum.isdigit() == False:
                    messages.error(request,"ID must be numbers only")
                    form = CreateTutor(request.POST,request.FILES)
                elif phone.isdigit() == False:
                    messages.error(request,"phone number must be must be numbers only")
                    form = CreateTutor(request.POST,request.FILES)
                elif len(phone) !=10:
                    messages.error(request,"phone number must be 10 numbers")
                elif not any(char in special_Sym for char in p1):#if password does'nt have any special character
                    messages.error(request,"Password must have a special Character @!$#")
                    form = CreateTutor(request.POST,request.FILES)
                elif User.objects.filter(email=e):#if email already exists
                    messages.error(request,"Email already exists")
                    form = CreateTutor(request.POST,request.FILES)
                elif User.objects.filter(username=un):#if username already exists
                    messages.error(request,"Username already exists")
                    form = CreateTutor(request.POST,request.FILES)
                elif un == "":#if username is empty
                    messages.error(request,"Username is empty")
                    form =CreateTutor(request.POST,request.FILES)
                elif len(un) < 4:#if username is too short
                    messages.error(request,"Username is too short must be more than 4 characters")
                    form =CreateTutor(request.POST,request.FILES)
                else:
                    u = User.objects.create_user(un,e,p1)
                    u.first_name = fname
                    u.last_name = lname
                    u.is_Tutor = True
                    u.user_id_num = id_num
                    u.user_dob = za_dob
                    u.user_age = za_age
                    u.save()
                    tutDet  = Tutors.objects.create(user=u)
                    tutDet.save()
                    Tutors(user=u,phone_num=phone,location=locate,img=img,qualification = quali,
                    subject=final_subj,fee_field=fee,Experiance= exp,gender=za_gender,tutoring_location = tut_loc,
                    serv_desc=service_desc,facebook_link=facebook_link,instagram_link=instagram_link,linkedin_link=linkedin_link,level=level,price_range=price_range).save()
                    
                    

                    messages.success(request," You are now a Tutor")
                    template = render_to_string('base/email_tutor.html',{'name':u.first_name})

                    send_mail(
                        'Thank you for Registering as a Tutor',
                        template, 
                        settings.EMAIL_HOST_USER,
                        [e], 
                        fail_silently=False,
                        )
                    return redirect("signin")
            except Exception as e:
                print(e)
    else:
        form = CreateTutor(request.POST,request.FILES)
        
    context = {"form": form}

    return render(request,"base/regTutor.html",context)


def RegStud(request):
    if request.method == "POST":
        
        formStud = CreateStud(request.POST,request.FILES)
      
        if formStud.is_valid():
            
            un = formStud.cleaned_data["username"]
            id_num = formStud.cleaned_data["id_num"]
            fname = formStud.cleaned_data["fname"]
            lname = formStud.cleaned_data["lname"]
            e = formStud.cleaned_data["email"]
            p1 = formStud.cleaned_data["pass1"]
            p2 = formStud.cleaned_data["pass2"]
            phone = formStud.cleaned_data["phone"]
            img_f = formStud.cleaned_data["img_field"]
            province = formStud.cleaned_data["location"]

            idnum = "".join(str(id_num))
            
            dob = idnum
            za_id = SouthAfricanIdentityValidate(idnum)
            valid = za_id.validate()
            za_gender = za_id.get_gender()
            za_age = za_id.get_age()
            za_dob = za_id.calculate_birthday()

            try:
                special_Sym = ["@","!","$","#"]
                if p1 != p2:#if passwords are not equal
                    messages.error(request,"Passwords are not equal")
                    formStud = CreateStud(request.POST,request.FILES)
                elif fname=="":
                    messages.error(request,"Enter your name")
                    form = CreateTutor(request.POST,request.FILES)
                elif lname=="":
                    messages.error(request,"Enter your last name")
                    form = CreateTutor(request.POST,request.FILES)
                elif not valid:
                    messages.error(request,"Your ID is not valid")
                    form = CreateTutor(request.POST,request.FILES)
                elif len(id_num) != 13:#if id is too short
                    messages.error(request,"ID is not 13 numbers")
                    formStud = CreateStud(request.POST,request.FILES)
                elif len(p1) < 6:#if password is too short
                    messages.error(request,"Password is too short must be more than 6 characters")
                    formStud = CreateStud(request.POST,request.FILES)
                elif idnum.isdigit() == False:
                    messages.error(request,"ID must be numbers only")
                elif phone.isdigit() == False:
                    messages.error(request,"phone number must be must be numbers only")
                    form = CreateTutor(request.POST,request.FILES)
                elif len(phone) !=10:
                    messages.error(request,"phone number must be 10 numbers")
                elif not any(char in special_Sym for char in p1):#if password does'nt have any special character
                    messages.error(request,"Password must have a special Character @!$#")
                    formStud = CreateStud(request.POST,request.FILES)
                elif User.objects.filter(email=e):#if email already exists
                    messages.error(request,"Email already exists")
                    formStud = CreateStud(request.POST,request.FILES)
                elif e=='':#if email is empty
                    messages.error(request,"Please enter you email")
                    formStud = CreateStud(request.POST,request.FILES)
                elif User.objects.filter(username=un):#if username already exists
                    messages.error(request,"Username already exists")
                    formStud = CreateStud(request.POST,request.FILES)
                elif un == "":#if username is empty
                    messages.error(request,"Username is empty")
                    formStud = CreateStud(request.POST,request.FILES)
                elif len(un) < 4:#if username is too short
                    messages.error(request,"Username is too short must be more than 4 characters")
                    formStud = CreateStud(request.POST,request.FILES)
                else:

                    u = User.objects.create_user(un,e,p1)
                    u.first_name = fname
                    u.last_name = lname
                    u.is_Student = True
                    u.user_id_num = id_num
                    u.user_dob = za_dob
                    u.user_age = za_age
                    u.save()

                    studDet  = Students.objects.create(user=u)
                    studDet.save()
                    Students(user=u,phone_num=phone,img=img_f,gender=za_gender,location=province).save()

                    messages.success(request," You are now a Student")

                    template = render_to_string('base/email_template.html',{'name':u.first_name})

                    send_mail(
                        'Thank you for Registering as a Student',
                        template,
                        settings.EMAIL_HOST_USER,
                        [e], 
                        fail_silently=False,
                        )
                    return redirect("signin")
            except Exception as e:
                print(e)

    else:
        formStud = CreateStud(request.POST,request.FILES)
       
    context = {"form": formStud}
    return render(request,"base/regStud.html",context)

@login_required(login_url ='signin')
def Profile(request):
    user = request.user
    
    context= {}
    if user.is_Student:
        query = Students.objects.get(user_id = user.id )
        context ={"query": query}
    elif user.is_Tutor:
        query = Tutors.objects.get(user_id =user.id )
        context ={"query": query}
   
    return render(request,"base/Profile.html",context)

@login_required(login_url ='signin')
def tutorProfile(request,pk):
    context= {}
    
    query = Tutors.objects.get(user_id =pk )
    context ={"query": query}
   
    return render(request,"base/tutorProfile.html",context)

@login_required(login_url ='signin')
def editProfile(request): 
    
    if request.method =="POST":
        context= {}
        user = request.user
        form = EditUser(request.POST,request.FILES)
        if form.is_valid():
            un = form.cleaned_data["username"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            e = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            
            u =  User.objects.get(id = user.id)

            if un != "":
                u.username = un
            elif User.objects.filter(username=un):
                messages.error(request,"Username has been taken")
                form = EditUser(request.POST)
            else:
                un = u.username

            if fname != "":
                u.first_name = fname
            else:
                fname = u.first_name
            
            if lname != "":
                u.last_name = lname
            else:
                lname = u.last_name
            
            if e != "":
                u.email = e
            else:
                un = u.email
            
            student_to_update = Students.objects.get(user_id = user.id )

            if phone != "":
                student_to_update.phone_num = phone
            else:
                phone = student_to_update.phone_num
            
            u.save()
            student_to_update.save()
        return redirect("Profile")
                
    else:
        form = EditUser(request.POST)
        
        
    context = {"form" : form}
    
    return render(request,"base/editProfile.html",context)

@login_required(login_url ='signin')
def editTutorProfile(request): 
    if request.method =="POST":
            context= {}
            user = request.user
            if user.is_Tutor:
                form = editTutor(request.POST, request.FILES)
                if form.is_valid():
                    un = form.cleaned_data["username"]
                    fname = form.cleaned_data["fname"]
                    lname = form.cleaned_data["lname"]
                    e = form.cleaned_data["email"]
                    phone = form.cleaned_data["phone"]
                    locate = form.cleaned_data["location"]
                    quali = form.cleaned_data["qualification"]
                   
                    fee = form.cleaned_data["fee"]
                    exp = form.cleaned_data["experiance"]
                    tut_loc = form.cleaned_data["tut_loc"]
                    img_f = form.cleaned_data["img_field"]
                    service_desc = form.cleaned_data["service_desc"]
                    facebook_link = form.cleaned_data["facebook_link"]
                    instagram_link = form.cleaned_data["instagram_link"]
                    linkedin_link = form.cleaned_data["linkedin_link"]
                    subj = request.session["subject"]
                    subj_2 = request.session["subject_2"]
                    level = request.session['level']
                    

                    if subj == []:
                        final_subj = subj_2
                    else:
                        final_subj = subj

                    u =  User.objects.get(id = user.id)
                   
                    if un != "":
                        u.username = un
                    elif User.objects.filter(username=un):
                        messages.error(request,"Username has been taken")
                        form = editTutor(request.POST,request.FILES)
                    else:
                        un = u.username

                    if fname != "":
                        u.first_name = fname
                    else:
                        fname = u.first_name
                    
                    if lname != "":
                        u.last_name = lname
                    else:
                        lname = u.last_name
                    
                    if e != "":
                        u.email = e
                    else:
                        e = u.email

                    tutor_to_update = Tutors.objects.get(user_id = user.id )
                    tutor_to_update.img = img_f
                    if phone != "":
                        tutor_to_update.phone_num = phone
                    else:
                        phone = tutor_to_update.phone_num
                    
                    if locate != "Other":
                        tutor_to_update.location = locate
                    else:
                        locate = tutor_to_update.location
                    
                    if quali != "":
                        tutor_to_update.qualification = quali
                    else:
                        quali = tutor_to_update.qualification
                    
                    if final_subj != "":
                        tutor_to_update.subject = final_subj
                    else:
                        final_subj = tutor_to_update.subject
                    
                    if level != "":
                        tutor_to_update.level = level
                    else:
                        level = tutor_to_update.level

                    if fee != "":
                        tutor_to_update.fee_field  = fee
                    else:
                        fee = tutor_to_update.fee_field
                    
                    if exp != "":
                        tutor_to_update.Experiance  = exp
                    else:
                        exp = tutor_to_update.Experiance
                    
                    if tut_loc != "------":
                        tutor_to_update.tutoring_location = tut_loc
                    else:
                        tut_loc = tutor_to_update.tutoring_location

                    if service_desc != "":
                        tutor_to_update.serv_desc= service_desc
                    else:
                        service_desc = tutor_to_update.serv_desc

                    if facebook_link != "":
                        tutor_to_update.facebook_link = facebook_link
                    else:
                        facebook_link = tutor_to_update.facebook_link
                    if img_f is not None:
                        tutor_to_update.img = img_f
                    else:
                        img_f = tutor_to_update.img

                    if instagram_link != "":
                        tutor_to_update.instagram_link  = instagram_link
                    else:
                        instagram_link = tutor_to_update.instagram_link
                    
                    if linkedin_link != "":
                        tutor_to_update.linkedin_link  = linkedin_link
                    else:
                        linkedin_link = tutor_to_update.linkedin_link
                    print(final_subj)
                    print(level)
                    #bprint(tutor_to_update.fee_field)
                    #print(fee)
                    u.save()
                    tutor_to_update.save()

                return redirect("Profile")
                
    else:
       form = editTutor(request.POST,request.FILES)
        
    context = {"form" : form}
    
    return render(request,"base/editTutorProfile.html",context)

@login_required(login_url ='signin')
def delUser(request):

    if request.method == "POST":
        del_form = DeleteUser(request.POST)
        user = request.user
        
        if user.is_Student:
            st = Students.objects.get(user_id = user.id )
            st.delete()
            user.delete()
        elif user.is_Tutor:
            tut = Tutors.objects.get(user_id =user.id )
            tut.delete()
            user.delete()
            messages.success(request,"Account Has been deleted")

            return redirect("signin")
    else:
        del_form = DeleteUser(request.POST)
    
    context = {
        "del_form":del_form
    }

    return render(request,"base/delUser.html",context)
@login_required(login_url ='signin')
def help(request):

    return render(request,"base/help.html")

def signout(request):
    logout(request)

    return redirect("signin")


def send_email(request):
    if request.method == "POST":
        send_email_form = Send_Email(request.POST)
        if send_email_form.is_valid():
            fname = send_email_form.cleaned_data["fname"]
            lname = send_email_form.cleaned_data["lname"]
            from_email = send_email_form.cleaned_data["from_email"]
            to_email = send_email_form.cleaned_data["to_email"]
            subj = request.session["subject"]
            subj_2 = request.session["subject_2"]
            serv_focus = send_email_form.cleaned_data["service_focus"]
            
            final_subj = ""
            if subj == []:
                final_subj = subj_2
            else:
                final_subj = subj

            if fname == "":
                messages.error(request,"Please Enter your name ")
                Send_Email(request.POST)
            elif lname == "":
                messages.error(request,"Please Enter your surname ")
                Send_Email(request.POST)
            elif from_email == "":
                messages.error(request,"Please Enter your email ")
                Send_Email(request.POST)
            elif to_email == "":
                messages.error(request,"Please Enter tutors email ")
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email):#if email already exists
                messages.error(request,"Tutor email does not exist")
                Send_Email(request.POST)
            elif not User.objects.filter(email=from_email):#if email already exists
                messages.error(request,"Student email does not exist")
                Send_Email(request.POST)
            else:    
                subjects = f'Hello my name is {fname} {lname}\n i would like to have tutouring sessions in this subject/subjects {final_subj} \n\n Here is my email {from_email}'
                focus = serv_focus
                send_mail(
                    'Request for tutoring session',
                    subjects +"\n \n"+ focus,
                    from_email,
                    [to_email,from_email], 
                    fail_silently=False,
                )
                return redirect("success")
    else:
        send_email_form = Send_Email(request.POST)
        
    context = {"send_email_form" : send_email_form}
    
    return render(request,"base/send_email.html",context)

def email_to_student(request):
    if request.method == "POST":
        send_student_email_form = Send_Student_Email(request.POST)
        if send_student_email_form.is_valid():
            fname = send_student_email_form.cleaned_data["fname"]
            lname = send_student_email_form.cleaned_data["lname"]
            from_email = send_student_email_form.cleaned_data["from_email"]
            to_email1 = send_student_email_form.cleaned_data["to_email1"]
            to_email2 = send_student_email_form.cleaned_data["to_email2"]
            to_email3 = send_student_email_form.cleaned_data["to_email3"]
            to_email4 = send_student_email_form.cleaned_data["to_email4"]
            to_email5 = send_student_email_form.cleaned_data["to_email5"]
            to_email6 = send_student_email_form.cleaned_data["to_email6"]
            to_email7 = send_student_email_form.cleaned_data["to_email7"]
            to_email8 = send_student_email_form.cleaned_data["to_email8"]
            to_email9 = send_student_email_form.cleaned_data["to_email9"]
            to_email10 = send_student_email_form.cleaned_data["to_email10"]
            to_email11 = send_student_email_form.cleaned_data["to_email11"]
            to_email12 = send_student_email_form.cleaned_data["to_email12"]
            to_email13 = send_student_email_form.cleaned_data["to_email13"]
            to_email14 = send_student_email_form.cleaned_data["to_email14"]
            to_email15 = send_student_email_form.cleaned_data["to_email15"]
            subj = request.session["subject"]
            subj_2 = request.session["subject_2"]
            ms_teams_link = send_student_email_form.cleaned_data["ms_teams_link"]
            serv_focus = send_student_email_form.cleaned_data["service_focus"]
            date = send_student_email_form.cleaned_data["date"]
            Time = send_student_email_form.cleaned_data["Time"]
            
            final_subj = ""
            if subj == []:
                final_subj = subj_2
            else:
                final_subj = subj

            email_list = []
            
            
            if to_email1 != "":
                email_list.append(to_email1)
            if to_email2!= "":
                email_list.append(to_email2)
            if to_email3 != "":
                email_list.append(to_email3)
            if to_email4 != "":
                email_list.append(to_email4)
            if to_email5 != "":
                email_list.append(to_email5)
            if to_email6 != "":
                email_list.append(to_email6)
            if to_email7 != "":
                email_list.append(to_email7)
            if to_email8 != "":
                email_list.append(to_email8)
            if to_email9 != "":
                email_list.append(to_email9)
            if to_email10 != "":
                email_list.append(to_email10)
            if to_email11 != "":
                email_list.append(to_email11)    
            if to_email12 != "":
                email_list.append(to_email12)
            if to_email13 != "":
                email_list.append(to_emai113)
            if to_email14 != "":
                email_list.append(to_email14)
            if to_email15 != "":
                email_list.append(to_email15)

            if fname == "":
                messages.error(request,"Please Enter your name ")
                Send_Student_Email(request.POST)
            elif lname == "":
                messages.error(request,"Please Enter your surname ")
                Send_Student_Email(request.POST)
            elif ms_teams_link == "":
                messages.error(request,"Please Enter your ms teams link ")
                Send_Student_Email(request.POST)
            elif date is None:
                messages.error(request,"Please Enter the date of the meeting")
                Send_Student_Email(request.POST)
            elif Time is None:
                messages.error(request,"Please Enter the time of the meeting")
                Send_Student_Email(request.POST)
            elif serv_focus == "":
                messages.error(request,"Please specify details of meeting")
                Send_Student_Email(request.POST)
            elif not User.objects.filter(email=from_email):#if email already exists
                messages.error(request,"Tutor email does not exist")
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email1):#if email already exists
                messages.error(request,f'{to_email1} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email2):#if email already exists
                messages.error(request,f'{to_email2} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email3):#if email already exists
                messages.error(request,f'{to_email3} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email4):#if email already exists
                messages.error(request,f'{to_email4} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email5):#if email already exists
                messages.error(request,f'{to_email5} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email6):#if email already exists
                messages.error(request,f'{to_email6} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email7):#if email already exists
                messages.error(request,f'{to_email7} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email8):#if email already exists
                messages.error(request,f'{to_email8} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email9):#if email already exists
                messages.error(request,f'{to_email9} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email10):#if email already exists
                messages.error(request,f'{to_email10} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email11):#if email already exists
                messages.error(request,f'{to_email11} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email12):#if email already exists
                messages.error(request,f'{to_email12} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email13):#if email already exists
                messages.error(request,f'{to_email13} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email14):#if email already exists
                messages.error(request,f'{to_email14} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email15):#if email already exists
                messages.error(request,f'{to_email15} email does not exist')
                Send_Email(request.POST)
            else:
                print(email_list)
                subjects = f'Hello my name is {fname} {lname}\n \nI am a tutor from MyTutorFinder and i would like to have an introduction meeting with you on Microsoft teams in this subject/subjects {final_subj} \n here is the tutors email: {from_email} \n Date of the meeting: \n {date} \n Time of the meeting: {Time}'
                link = ms_teams_link
                details = serv_focus
            
                send_mail(
                    'Tutor Introduction Meeting',
                    subjects +"\n" + "\n join the microsoft teams link below \n" +link+ "\n" + "\n" + details,
                    from_email,
                    email_list, 
                    fail_silently=False,
                    )
                
                return redirect("success")

    else:
        
        send_student_email_form = Send_Student_Email(request.POST)
        
    context = {"send_student_email_form" : send_student_email_form}
    
    return render(request,"base/email_to_student.html",context)
             

def reject_request(request):
    if request.method == "POST":
        reject_form = Reject_Email(request.POST)
        if reject_form.is_valid():
            fname =reject_form.cleaned_data["fname"]
            lname = reject_form.cleaned_data["lname"]
            from_email = reject_form.cleaned_data["from_email"]
            to_email1 = reject_form.cleaned_data["to_email1"]
            to_email2 = reject_form.cleaned_data["to_email2"]
            to_email3 = reject_form.cleaned_data["to_email3"]
            to_email4 = reject_form.cleaned_data["to_email4"]
            to_email5 = reject_form.cleaned_data["to_email5"]
            to_email6 = reject_form.cleaned_data["to_email6"]
            to_email7 = reject_form.cleaned_data["to_email7"]
            to_email8 = reject_form.cleaned_data["to_email8"]
            to_email9 = reject_form.cleaned_data["to_email9"]
            to_email10 = reject_form.cleaned_data["to_email10"]
            to_email11 = reject_form.cleaned_data["to_email11"]
            to_email12 = reject_form.cleaned_data["to_email12"]
            to_email13 = reject_form.cleaned_data["to_email13"]
            to_email14 = reject_form.cleaned_data["to_email14"]
            to_email15 = reject_form.cleaned_data["to_email15"]


            email_list = []
            
            
            if to_email1 != "":
                email_list.append(to_email1)
            if to_email2!= "":
                email_list.append(to_email2)
            if to_email3 != "":
                email_list.append(to_email3)
            if to_email4 != "":
                email_list.append(to_email4)
            if to_email5 != "":
                email_list.append(to_email5)
            if to_email6 != "":
                email_list.append(to_email6)
            if to_email7 != "":
                email_list.append(to_email7)
            if to_email8 != "":
                email_list.append(to_email8)
            if to_email9 != "":
                email_list.append(to_email9)
            if to_email10 != "":
                email_list.append(to_email10)
            if to_email11 != "":
                email_list.append(to_emai11)    
            if to_email12 != "":
                email_list.append(to_email12)
            if to_email13 != "":
                email_list.append(to_emai13)
            if to_email14 != "":
                email_list.append(to_email14)
            if to_email15 != "":
                email_list.append(to_email15)

            if fname == "":
                messages.error(request,"Please Enter your name ")
                Reject_Email(request.POST)
            elif lname == "":
                messages.error(request,"Please Enter your surname ")
                Reject_Email(request.POST)
            elif not User.objects.filter(email=from_email):
                messages.error(request,"Tutor email does not exist")
                Reject_Email(request.POST)
            elif not User.objects.filter(email=to_email1):#if email already exists
                messages.error(request,f'{to_email11} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email2):#if email already exists
                messages.error(request,f'{to_email12} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email3):#if email already exists
                messages.error(request,f'{to_email3} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email4):#if email already exists
                messages.error(request,f'{to_email4} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email5):#if email already exists
                messages.error(request,f'{to_email5} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email6):#if email already exists
                messages.error(request,f'{to_email6} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email7):#if email already exists
                messages.error(request,f'{to_email7} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email8):#if email already exists
                messages.error(request,f'{to_email8} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email9):#if email already exists
                messages.error(request,f'{to_email9} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email10):#if email already exists
                messages.error(request,f'{to_email10} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email11):#if email already exists
                messages.error(request,f'{to_email11} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email12):#if email already exists
                messages.error(request,f'{to_email12} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email13):#if email already exists
                messages.error(request,f'{to_email13} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email14):#if email already exists
                messages.error(request,f'{to_email14} email does not exist')
                Send_Email(request.POST)
            elif not User.objects.filter(email=to_email15):#if email already exists
                messages.error(request,f'{to_email15} email does not exist')
                Send_Email(request.POST)
            else:
                print(email_list)
                subjects = f'Hello my name is {fname} {lname}\n \n We would like to inform you that your Request for a tutor has been regected by the tutor.\n'
            
                send_mail(
                    'Tutor Request Regected',
                    subjects,
                    from_email,
                    email_list, 
                    fail_silently=False,
                    )
                
                return redirect("Profile")

    else:
        
        reject_form = Reject_Email(request.POST)
        
    context = {"reject_form" : reject_form}
    
    return render(request,"base/reject_request.html",context)
             
