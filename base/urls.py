from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home" ),
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
    
    path('help/', views.help,name="help"),
    path('how_it_works/', views.how_it_works,name="how_it_works"),

    path('instructions_stud/', views.instructions_stud,name="instructions_stud"),
    path('instructions_tut/', views.instructions_tut,name="instructions_tut"),

    path('subject_choice_stud/',views.subject_choice_stud,name="subject_choice_stud"),
    path('subject_choice_tut/',views.subject_choice_tut,name="subject_choice_tut"),
    path('subject_choice/',views.subject_choice,name="subject_choice"),
    path('subject_update/',views.subject_update,name="subject_update"),

    path('send_email/', views.send_email,name="send_email"),
    path('email_to_student/',views.email_to_student,name="email_to_student"),
    path('reject_request/',views.reject_request,name="reject_request"),

    path('success/', views.success,name="success"),
    path('editProfile/', views.editProfile,name="editProfile"),
    path('editTutorProfile/', views.editTutorProfile,name="editTutorProfile"),

    path('RegTut/', views.RegTut,name= "RegTut"),
    path('RegStud/', views.RegStud,name= "RegStud"),
    path('display_subjects/', views.display_subjects,name="display_subjects"),

    path('Profile/', views.Profile,name="Profile"),
    path('tutorProfile/<str:pk>/', views.tutorProfile,name="tutorProfile"),

    path('delUser/', views.delUser,name= "delUser"),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset_form.html")
    ,name="password_reset_confirm"),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset_done.html"),
    name="password_reset_complete"),

]
 
'''
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
'''