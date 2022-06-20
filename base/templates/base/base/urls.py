from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home" ),
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
    path('help/', views.help,name="help"),
    path('send_email/', views.send_email,name="send_email"),
    path('email_to_student/',views.email_to_student,name="email_to_student"),

    path('editProfile/', views.editProfile,name="editProfile"),
    path('editTutorProfile/', views.editTutorProfile,name="editTutorProfile"),

    path('RegTut/', views.RegTut,name= "RegTut"),
    path('RegStud/', views.RegStud,name= "RegStud"),

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