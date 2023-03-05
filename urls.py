"""admission_blockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from mainapp import views as mainapp_views
from studentapp import views as studentapp_views
from adminapp import views as adminapp_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    
    #  main page
    path('', mainapp_views.main_home,name='main_home'),
    path('main-about',mainapp_views.main_about,name='main_about'),
    path('main-contact',mainapp_views.main_contact,name='main_contact'),
   
    
    
    # student page 
     path('main-studentregistration',studentapp_views.main_studentregistration,name='main_studentregistration'),
    path('main-studentlogin',studentapp_views.main_studentlogin,name='main_studentlogin'),
    path('student-dashboard',studentapp_views.student_dashboard,name='student_dashboard'),
    path('student-courses',studentapp_views.student_courses,name='student_courses'),
    path('student-application/<int:id>',studentapp_views.student_application,name='student_application'),
    path('student-myprofile',studentapp_views.student_myprofile,name='student_myprofile'),
    
    
    
    # admin page
    path('main-adminlogin',adminapp_views.main_adminlogin,name='main_adminlogin'),
    path('admin-dashboard',adminapp_views.admin_dashboard,name='admin_dashboard'),
    path('admin-addcourse',adminapp_views.admin_addcourse,name='admin_addcourse'),
    path('admin-editmanagecourse/<int:id>',adminapp_views.admin_editmanagecourse,name='admin_editmanagecourse'),
    path('admin-managecourse',adminapp_views.admin_managecourse,name='admin_managecourse'),
    path('admin-viewaccepted',adminapp_views.admin_viewaccepted,name='admin_viewaccepted'),
    path('admin-viewinvalidapplication',adminapp_views.admin_viewinvalidapplication,name='admin_viewinvalidapplication'),
    path('admin-viewpendingapplication',adminapp_views.admin_viewpendingapplication,name='admin_viewpendingapplication'),
    path('accept_application/<int:id>',adminapp_views.accept_application,name="accept_application"),
    path('reject_application/<int:id>',adminapp_views.reject_application,name="reject_application"),
    path('verify_application/<int:id>',adminapp_views.verify_application,name="verify_application"),
    path('admin-viewstudent',adminapp_views.admin_viewstudent,name='admin_viewstudent'),
    path('admin-logout',adminapp_views.admin_viewstudent,name="admin_logout"),
    # path('admin-verify/<int:id>',adminapp_views.admin_verify,name="admin_verify")
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
