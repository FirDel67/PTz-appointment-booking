from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import base64
import qrcode
from io import BytesIO
from django.core.files import File


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=255, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_patient = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)


class Clinic(models.Model):
    user = models.ForeignKey(CustomUser, related_name="clinic", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Clinic {self.name} located at {self.address}"
    

class Doctor(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="doctors")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialty}"


class Availability(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinic_availabilities')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    day = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('clinic', 'doctor', 'date', 'start_time')

    def __str__(self):
        return f"{self.doctor.first_name + self.doctor.last_name} is available on {self.date} from {self.start_time} to {self.end_time}"
    
    def save(self, *args, **kwargs):
        self.day = self.date.strftime("%A")
        super().save(*args, **kwargs)


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]
    
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="clinic_appointments")
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient_appointments', 
                                null=True, blank=True, default=None)
    patient_email = models.EmailField(null=True, blank=True, default=None)
    patient_phone = models.CharField(max_length=50, null=True, blank=True, default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='dr_appointments')
    date = models.DateField()
    time = models.TimeField()
    ticket_id = models.CharField(max_length=50, editable=False, unique=True, default=None)
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    status_changed_at = models.DateTimeField(null=True, blank=True)
    
    canceled_at = models.DateTimeField(null=True, blank=True)
    rescheduled_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Ticket-specific fields
    issued_at = models.DateTimeField(null=True, blank=True)
    qr_code = models.ImageField(upload_to='tickets/', blank=True, null=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.first_name} {self.doctor.last_name} for {self.patient.username if self.patient else self.patient_contact} on {self.date} at {self.time}"

    def save(self, *args, **kwargs):
        random_code = str(uuid.uuid4()).replace('-', '')[:10].upper()
        if not self.ticket_id:
            self.ticket_id = f"{self.clinic.name[:3]}-{random_code}"
            while Appointment.objects.filter(ticket_id=self.ticket_id).exists():
                self.ticket_id = f"{self.clinic.name[:3]}-{random_code}"
        
        if not self.qr_code:
            self.qr_code = self.generate_qr_code()    
        
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        qr_data = f"Appointment Ticket ID: {self.ticket_id} - {self.date} at {self.time} - Status: {self.status}"
        qr = qrcode.make(qr_data)
        qr_io = BytesIO()
        qr.save(qr_io, 'PNG')
        qr_io.seek(0)  # Ensure the file pointer is at the start of the QR code image
        return File(qr_io, name=f"{self.ticket_id}_qr.png")

    def send_ticket_email(self, request):
        subject = f'Your Appointment Ticket - {self.clinic.name}'
        logo_url = request.build_absolute_uri(settings.STATIC_URL + 'img/logo.jpeg')
        
        # Get recipient email
        recipient_mail = self.patient_email if self.patient_email else self.patient.email

        # Convert QR code image to base64
        qr_image = self.qr_code
        if qr_image:
            with qr_image.open('rb') as image_file:
                qr_image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        else:
            qr_image_base64 = None  # Fallback if QR code is missing
            
        if self.qr_code:
            qr_code_url = request.build_absolute_uri(self.qr_code.url)

         # Choose template and subject based on status
        if self.status == "pending":
            subject = f'Appointment Booked - {self.clinic.name} (Pending Confirmation)'
            template = 'emails/ticket_email.html'
            print("Emails/ticket_email.html")
        elif self.status == "confirmed":
            subject = f'Appointment Confirmed - {self.clinic.name}'
            template = 'emails/ticket_confirmed_email.html'
            print("emails/ticket_confirmed_email.html")
        elif self.status == "cancelled":
            subject = f'Appointment Cancelled - {self.clinic.name}'
            template = 'emails/ticket_cancelled_email.html'
            print("emails/ticket_cancelled_email.html")
        else:
            # Default case (unlikely to be hit unless a new status is added)
            subject = f'Appointment Booked - {self.clinic.name} (Pending Confirmation)'
            template = 'emails/ticket_email.html'

        # Render HTML email with embedded QR code
        html_message = render_to_string(template, {
            'patient': self.patient.username if self.patient else self.patient_email,
            'doctor_name': f"{self.doctor.first_name} {self.doctor.last_name}",
            'clinic_name': self.clinic.name,
            'date': self.date,
            'time': self.time,
            'address': self.clinic.address,
            'phone': self.clinic.phone,
            'email': self.clinic.email,
            'ticket_id': self.ticket_id,
            'logo_url': logo_url,
            'status': self.status,
            'qr_code_base64': qr_code_url,
        })
        
        # Fallback for email clients that don’t support HTML
        plain_message = strip_tags(html_message)
        
        # Send email with embedded QR code
        try:
            send_mail(
                subject,
                plain_message,
                settings.EMAIL_HOST_USER,
                [recipient_mail],
                html_message=html_message,
            )
            print("Email sent to patient")
        except Exception as e:
            print(f"Failed to send email: {e}")
        
    def send_notification_to_doctor(self, request):
        
        subject = f'New Appointment Booked - {self.clinic.name}'
        logo_url = request.build_absolute_uri(settings.STATIC_URL + 'img/logo.jpeg')

        html_message = render_to_string('emails/notification_email.html', {
            'doctor_name': self.doctor.first_name,
            'patient_name': self.patient.username if self.patient else self.patient_email,
            'patient_ticket': self.ticket_id,
            'date': self.date,
            'time': self.time,
            'status': self.status,
            'clinic_name': self.clinic.name,
            'logo_url': logo_url,
        })
        plain_message = strip_tags(html_message)

        try:
            send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [self.doctor.email], html_message=html_message)
            print(f"Notification sent to {self.doctor.email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def update_status(self, new_status, request):
        """
        Updates the appointment status, manages ticket issuance or cancellation actions, and
        handles notification emails to the patient.
        """
        self.status = new_status

        if new_status == 'confirmed':
            if not self.issued_at:
                self.issued_at = timezone.now()
                self.send_ticket_email(request)
                self.send_notification_to_doctor(request)

        elif new_status == 'cancelled':
            self.cancel(request) 
            self.issued_at = None
            self.send_ticket_email(request)
  
        self.status_changed_at = timezone.now()
        self.save()

    def cancel(self, request):
        """
        Cancels the appointment and updates the cancellation timestamp. If the appointment was confirmed,
        a cancellation notification is sent to the doctor.
        """
        print("Self status: ", self.status, " -- Issued status: ", self.issued_at)
        if self.status == 'confirmed' or self.issued_at is not None:
            subject = f'Appointment Cancelled - {self.clinic.name}'
            logo_url = request.build_absolute_uri(settings.STATIC_URL + 'img/logo.jpeg')
            
            # Render HTML email for doctor notification
            html_message = render_to_string('emails/cancellation_notification_email.html', {
                'doctor_name': self.doctor.first_name,
                'patient_name': self.patient.username if self.patient else self.patient_email,
                'patient_ticket': self.ticket_id,
                'date': self.date,
                'time': self.time,
                'clinic_name': self.clinic.name,
                'address': self.clinic.address,
                'phone': self.clinic.phone,
                'email': self.clinic.email,
                'logo_url': logo_url,
            })
            plain_message = strip_tags(html_message)

            try:
                send_mail(
                    subject,
                    plain_message,
                    settings.EMAIL_HOST_USER,
                    [self.doctor.email],
                    html_message=html_message
                )
                print(f"Cancellation notification sent to {self.doctor.email}")
            except Exception as e:
                print(f"Failed to send email: {e}")
        
        # Update status and timestamps regardless of notification
        self.status = 'cancelled'
        self.canceled_at = timezone.now()
        self.save()

    def reschedule(self):
        self.rescheduled_at = timezone.now()
        self.status = 'pending'
        self.save()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


"""
    The key models we need are:

        1. Doctor: Information about each doctor.
        2. Availability: Store the available times for each doctor.
        3. Appointment: Store appointment details, including a ticket ID for the appointment.
        4. Patient: Store patient/user details (if not using Django’s User model directly).
""" 
