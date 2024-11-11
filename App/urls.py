from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("", HomePage, name="HomePage"),
    path("book_appointment/", Book_Appointment, name="book_appointment"),
    path('user/appointments/', user_appointments, name='user_appointments'),
    path('appointments/modify/<int:id>/', modify_appointment, name='modify_appointment'),
    path('appointments/delete/<int:id>/', delete_appointment, name='delete_appointment'),

    path('appointments/<str:ticket_id>/details/', appointment_detail, name='appointment_detail'),
    path('appointments/<str:ticket_id>/update-status/', update_appointment_status, name='update_appointment_status'),
    path('appointments/<str:ticket_id>/reschedule/', reschedule_appointment, name='reschedule_appointment'),
    
    path('clinic/<int:clinic_id>/appointments/', clinic_appointments, name='clinic_appointments'),
    path('clinic/appointment/<str:ticket_id>/details/', clinic_appointment_detail, name='clinic_appointment_detail'),
    
    # Clinic URLs
    path('your-clinic/', clinic_list, name='clinic_list'),
    path('clinic/create/', clinic_create, name='clinic_create'),
    path('clinic/<int:clinic_id>/update/', clinic_update, name='clinic_update'),
    path('clinic/<int:clinic_id>/delete/', clinic_delete, name='clinic_delete'),
    
    # Doctor URLs
    path('clinic/<int:clinic_id>/doctors/', doctor_list, name='doctor_list'),
    path('clinic/<int:clinic_id>/doctor/create/', doctor_create, name='doctor_create'),
    path('clinic/<int:clinic_id>/doctor/<int:doctor_id>/update/', doctor_update, name='doctor_update'),
    path('clinic/<int:clinic_id>/doctor/<int:doctor_id>/delete/', doctor_delete, name='doctor_delete'),
    
    # For Doctor's Availability
    path('clinic/<int:clinic_id>/doctor/<int:doctor_id>/add_availability/', add_availability, name='availability_add'),    
    path('clinic/<int:clinic_id>/doctor/<int:doctor_id>/details/', doctor_detail, name='doctor_detail'),
    path('availability/<int:availability_id>/update/', update_availability, name='availability_update'),
    path('availability/<int:availability_id>/delete/', delete_availability, name='availability_delete'),
    path('availability/<int:availability_id>/', get_availability, name='availability_detail'),

    path('about-us/', about_us, name='about_us'),
    path('contact/', contact_view, name='contact'),
    path('list/messages/', contact_list, name='contact_list'),
    path('contacts/reply/<int:contact_id>/', reply_contact, name='reply_contact'),
    
    # Account urls
    path('patient/login/', login_patient_view, name='patient_login_view'),
    path('register/patient/', register_patient_view, name='register_patient_view'),
    path('patient-account/details/', account_details_view, name='account_details_view'),
    path('patient/update/', update_patient_view, name='update_patient_view'),
    
    path('login/admin/', login_view, name='login_view'),
    path('register/admin/', register_admin_view, name='register_admin_view'),
    path('admin-account/details/', admin_account_details_view, name='admin_account_details_view'),
    path('update/admin/', update_admin_view, name='update_admin_view'),
    
    path('logout/', logout_view, name='logout'),
    
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)