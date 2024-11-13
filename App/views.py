<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> 183cd9f74c1f0208e0db6d8d08734a8984f0793d
from .models import Clinic, Doctor, Appointment, CustomUser, Availability, Contact
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login, logout
from .forms import UpdatePatientForm
from datetime import datetime
import json

<<<<<<< HEAD
=======

>>>>>>> 183cd9f74c1f0208e0db6d8d08734a8984f0793d
def HomePage(request):
    return render(request, 'App/home.html')

def Book_Appointment(request):
    clinic = Clinic.objects.get(pk=1)
    doctors = Doctor.objects.filter(clinic_id=clinic.id).all()
    availabilities = Availability.objects.filter(clinic_id=clinic, doctor__in=doctors)

    # Check for POST request
    if request.method == 'POST':
        clinic_id = clinic.id
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Check if the selected doctor is available
        availability_exists = Availability.objects.filter(
            doctor_id=doctor_id,
            date=date,
            start_time__lte=time,
            end_time__gte=time
        ).exists()
        
        doctor = Doctor.objects.get(pk=doctor_id)

        # Check if there’s an existing appointment for the same time
        if Appointment.objects.filter(doctor_id=doctor_id, date=date, time=time).exists():
            return JsonResponse({'status': 'error', 'message': 'Doctor is already booked for this date and time.'})

        if not availability_exists:
            return JsonResponse({'status': 'error', 'message': 'The selected doctor is not available at this time.'})

<<<<<<< HEAD
        try:
        # Create and save the appointment
            if email is not None or phone is not None:
                appointment = Appointment(
                    clinic_id=clinic_id,
                    doctor=doctor,
                    patient=request.user if request.user else None,
                    patient_email = email,
                    patient_phone= phone,
                    date=date,
                    time=time
                )
                appointment.save()
                appointment.send_ticket_email(request)
            else:
                appointment = Appointment(
                    clinic_id=clinic_id,
                    doctor=doctor,
                    patient=request.user,
                    date=date,
                    time=time
                )
                appointment.save()
                appointment.send_ticket_email(request)

            return JsonResponse({'status': 'success', 'message': 'Your appointment has been booked successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"An error occured: {str(e)}"})
=======
        # Create and save the appointment
        if email is not None or phone is not None or request.user:
            appointment = Appointment(
                clinic_id=clinic_id,
                doctor=doctor,
                patient=request.user if request.user else None,
                patient_email = email,
                patient_phone= phone,
                date=date,
                time=time
            )
            appointment.save()
            appointment.send_ticket_email(request)
        else:
            appointment = Appointment(
                clinic_id=clinic_id,
                doctor=doctor,
                patient=request.user,
                date=date,
                time=time
            )
            appointment.save()
            appointment.send_ticket_email(request)

        return JsonResponse({'status': 'success', 'message': 'Your appointment has been successfully booked!'})
>>>>>>> 183cd9f74c1f0208e0db6d8d08734a8984f0793d

    # For GET request, provide all available doctors and their availabilities
    return render(request, 'App/book_appointment.html', {
        'clinic': clinic,
        'doctors': doctors,
        'availabilities': availabilities
    })

@login_required(login_url='/patient/login/')
def modify_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    doctor_availability = Availability.objects.filter(doctor=appointment.doctor, date=appointment.date)
    
    is_admin = request.user.is_superuser or request.user.is_staff

    if request.method == 'POST':
        # Extract data from the request
        date = request.POST.get('date')
        time = request.POST.get('time')
        status = request.POST.get('status')

        # Check if the new date and time fall within the doctor's availability
        availability_exists = Availability.objects.filter(
            doctor=appointment.doctor,
            date=date,
            start_time__lte=time,
            end_time__gte=time
        ).exists()

        if not availability_exists:
            return JsonResponse({'status': 'error', 'message': 'The doctor is not available at the selected time.'})

        # Check for conflicting appointments
        if Appointment.objects.filter(
            doctor=appointment.doctor,
            date=date,
            time=time
        ).exclude(id=appointment.id).exists():
            return JsonResponse({'status': 'error', 'message': 'The doctor already has an appointment at this time.'})

        # Update appointment fields if no conflicts were found
        appointment.date = date
        appointment.time = time
        # if not is_admin and status in ['pending', 'cancelled']: 
        #     appointment.status = status
        # elif not is_admin and status not in ['pending', 'cancelled']:
        #     return JsonResponse({'status': 'error', 'message': 'You are not allowed to confirm the appointment'})
        # else:
        appointment.status = status
        appointment.save()

        return JsonResponse({'status': 'success', 'message': 'Your appointment has been successfully updated!'})

    # Pass existing appointment data and doctor's availability to the template for display
    return render(request, 'App/modify_appointment.html', {
        'appointment': appointment,
        'doctor_availability': doctor_availability
    })

@login_required(login_url='/patient/login/')
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == 'POST':
        try:
            appointment.delete()
            return JsonResponse({'status': 'success', 'message': 'Your appointment has been successfully deleted!'})
        except Exception as e:
            JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@login_required(login_url='/patient/login/')
def appointment_detail(request, ticket_id):
    appointment = get_object_or_404(Appointment, ticket_id=ticket_id)
    return render(request, 'App/appointment_detail.html', {'appointment': appointment})

def update_appointment_status(request, ticket_id):
    # Ensure the user is logged in and has permission to change the appointment status
    if not request.user.is_authenticated:
        return JsonResponse({'status': "error", "message": "You need to be logged in to update the appointment status."})

    appointment = get_object_or_404(Appointment, ticket_id=ticket_id)

    if request.method == 'POST':
        # Check for valid status update requests
        if 'confirm' in request.POST:
            if appointment.status == 'confirmed':
                return JsonResponse({'status': "error", "message": "This appointment is already confirmed."})
            appointment.update_status('confirmed', request)
            return JsonResponse({'status': "success", "message": f"Appointment {ticket_id} confirmed successfully."})

        elif 'cancel' in request.POST:
            if appointment.status == 'cancelled':
                return JsonResponse({'status': "error", "message": "This appointment is already cancelled."})
            appointment.update_status('cancelled', request)
            return JsonResponse({'status': "success", "message": f"Appointment {ticket_id} cancelled successfully."})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

def reschedule_appointment(request, ticket_id):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "You need to be logged in to reschedule the appointment."})

    appointment = get_object_or_404(Appointment, ticket_id=ticket_id)

    # Check if the appointment is cancelled before rescheduling
    if appointment.status != 'cancelled':
        return JsonResponse({"status": "error", "message": "Only cancelled appointments can be rescheduled."})
    
    appointment.reschedule()
    appointment.send_ticket_email(request)
    return JsonResponse({"status": "success", "message": f"Appointment {ticket_id} has been rescheduled successfully."})

@login_required(login_url='/patient/login/')
def user_appointments(request):
    # Get appointments specific to the logged-in user
    appointments = Appointment.objects.filter(patient=request.user).select_related('doctor', 'clinic')
    is_logged_in = request.user
    return render(request, 'App/user_appointments.html', {
        'appointments': appointments, 'is_logged_in': is_logged_in}
        )

@login_required(login_url='/login/admin/')
def clinic_appointments(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    appointments = Appointment.objects.filter(clinic_id=clinic_id).select_related('doctor', 'patient')
    return render(request, 'App/clinic_appointments.html', 
                  {'appointments': appointments, 'clinic': clinic}
                  )

@login_required(login_url='/login/admin/')
def clinic_appointment_detail(request, ticket_id):
    appointment = get_object_or_404(Appointment, ticket_id=ticket_id)
    return render(request, 'App/clinic_appointment_detail.html', {'appointment': appointment})

def about_us(request):
    clinic = Clinic.objects.get(pk=1)
    return render(request, 'App/about_us.html', {'clinic': clinic})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message')

        try:
            # Save to the database
            contact = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            # Prepare context for the email template
            context = {
                'name': name,
                'message': message,
                'year': datetime.now().year
            }

            # Render the HTML template as a string
            html_content = render_to_string('emails/contact_email.html', context)
            
            # Fallback for email clients that don’t support HTML
            plain_message = strip_tags(html_content)

            # Send email with HTML content
            subject = 'Thank you for contacting Polyclinique Tereziya'
            from_email = settings.EMAIL_HOST_USER
            recipient_mail = [email]
            
            try:
                send_mail(
                    subject,
                    plain_message,
                    from_email,
                    recipient_mail,
                    html_message=html_content,
                )
                print("Email sent successfully to user!")

                # Notify admin (Optional)
                admin_subject = 'New Contact Form Submission'
                admin_message = f"New message from {name} ({email}):\n\n{message}\n\nPhone: {phone}"
                send_mail(admin_subject, admin_message, from_email, [from_email, "shaddaifirst@gmail.com"], fail_silently=False)
                print("Mail sent successfully to admin!")

            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({'status': 'error', 'message': 'Failed to send email.'})
            
            return JsonResponse({'status': 'success', "message": "Your message has been received."})
        except Contact.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Failed to save contact information.'})
        except Exception as e:
            print(f"Error saving contact information: {e}")
            return JsonResponse({'status': 'error', 'message': 'Failed to save contact information.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

# List all clinics
@login_required(login_url='/login/admin/')
def clinic_list(request):
    clinic = Clinic.objects.get(pk=1)
    return render(request, 'clinic/clinic_list.html', {'clinic': clinic})

# Create a new clinic
@login_required(login_url='/login/admin/')
def clinic_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        opening_hours = request.POST.get('opening_hours')

        try:
            # Save the new clinic
            new_clinic = Clinic.objects.create(
                user=request.user,
                name=name,
                address=address,
                phone=phone,
                email=email,
                description=description,
                opening_hours=opening_hours
            )
            
            return JsonResponse({'status': 'success', "message": "Clinic created successfully!"})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to create clinic: {str(e)}"})

    return render(request, 'clinic/clinic_form.html')

# Update an existing clinic
@login_required(login_url='/login/admin/')
def clinic_update(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if request.method == 'POST':
        clinic.name = request.POST.get('name')
        clinic.address = request.POST.get('address')
        clinic.phone = request.POST.get('phone')
        clinic.email = request.POST.get('email')
        clinic.description = request.POST.get('description')
        clinic.opening_hours = request.POST.get('opening_hours')

        try:
            clinic.save()
            return JsonResponse({'status': 'success', "message": "Clinic updated successfully!"})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to update clinic: {str(e)}"})

    return render(request, 'clinic/clinic_form.html', {'clinic': clinic})

# Delete a clinic
@login_required(login_url='/login/admin/')
def clinic_delete(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if request.method == 'POST':
        try:
            clinic.delete()
            return JsonResponse({'status': "error", "message": "Clinic deleted successfully!"})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to delete clinic: {str(e)}"})
    
    return JsonResponse({'status': 'error', "message": "Invalid request"})

# List all doctors in a clinic
@login_required(login_url='/login/admin/')
def doctor_list(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    doctors = clinic.doctors.all()
    return render(request, 'doctor/doctor_list.html', {'clinic': clinic, 'doctors': doctors})

# Create a new doctor
@login_required(login_url='/login/admin/')
def doctor_create(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        specialty = request.POST.get('specialty')
        email = request.POST.get('email')

        try:
            new_doctor = Doctor.objects.create(
                clinic=clinic,
                first_name=first_name,
                last_name=last_name,
                specialty=specialty,
                email=email
            )
            return JsonResponse({'status': "success", "message": "Doctor created successfully!"})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to create doctor: {str(e)}"})

    return render(request, 'doctor/doctor_form.html', {'clinic': clinic})

# Update an existing doctor
@login_required(login_url='/login/admin/')
def doctor_update(request, clinic_id, doctor_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        doctor.first_name = request.POST.get('first_name')
        doctor.last_name = request.POST.get('last_name')
        doctor.specialty = request.POST.get('specialty')
        doctor.email = request.POST.get('email')

        try:
            doctor.save()
            return JsonResponse({"status": 'success', "message": "Doctor updated successfully!"})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to update doctor: {str(e)}"})

    return render(request, 'doctor/doctor_form.html', {'clinic': clinic, 'doctor': doctor})

# Delete a doctor
@login_required(login_url='/login/admin/')
def doctor_delete(request, clinic_id, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        try:
            doctor.delete()
            return JsonResponse({'status': 'success', "message": "Doctor deleted successfully!"})
        except  Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to delete doctor: {str(e)}"})
    
    return JsonResponse({'status': "error", 'message': 'Invalid request!'})

def doctor_detail(request, clinic_id, doctor_id):
    doctor = get_object_or_404(Doctor, clinic_id=clinic_id, id=doctor_id)
    availabilities = Availability.objects.filter(clinic_id=clinic_id, doctor_id=doctor_id).all()
    return render(request, 'doctor/doctor_detail.html', {
        'doctor': doctor,
        'availabilities': availabilities,
    })

@login_required(login_url='/login/admin/')
def add_availability(request, clinic_id, doctor_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # Validate required fields
        if not (date or start_time or end_time):
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'})

        try:
            # Create new availability
            new_availability = Availability.objects.create(
                clinic=clinic,
                doctor=doctor,
                date=date,
                start_time=start_time,
                end_time=end_time
            )
            print("New availability: ", new_availability)
            return JsonResponse({'status': 'success', 'message': 'Availability added successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Failed to add availability: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required(login_url='/login/admin/')
def update_availability(request, availability_id):
    availability = get_object_or_404(Availability, id=availability_id)
    
    if request.method == 'POST':
        date_str = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # Validate required fields
        if not (date_str and start_time and end_time):
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'})

        try:
            # Parse the date and update fields
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            availability.date = date_obj
            availability.day = date_obj.strftime('%A')  # e.g., Monday, Tuesday
            availability.start_time = start_time
            availability.end_time = end_time

            # Save the updated availability
            availability.save()
            return JsonResponse({'status': 'success', 'message': 'Availability updated successfully.'})
        except ValueError as ve:
            return JsonResponse({'status': 'error', 'message': f'Invalid date format: {str(ve)}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Failed to update availability: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required(login_url='/login/admin/')
def delete_availability(request, availability_id):
    availability = get_object_or_404(Availability, id=availability_id)
    
    if request.method == "POST":
        try:
            availability.delete()
            return JsonResponse({"status": "success", 'message': 'Availability deleted successfully.'})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f'Failed to delete availability: {str(e)}'})
    
    return JsonResponse({"status": 'error', "message": 'Invalid request method.'})

@login_required(login_url='/login/admin/')
def get_availability(request, availability_id):
    availability = get_object_or_404(Availability, id=availability_id)
    data = {
        'date': availability.date,
        'start_time': availability.start_time,
        'end_time': availability.end_time
    }
    return JsonResponse(data)

@login_required(login_url='/login/admin/')
def admin_dashboard(request):
    user = CustomUser.objects.get(pk=1)
    clinic = Clinic.objects.get(pk=1)
    doctors = Doctor.objects.filter(clinic_id=clinic).count()
    total_appointments = Appointment.objects.count()
    pending_appointments = Appointment.objects.filter(status='pending').count()
    cancelled_appointments = Appointment.objects.filter(status='cancelled').count()
    confirmed_appointments = Appointment.objects.filter(status='confirmed').count()
    messages = Contact.objects.count()

    return render(request, 'Admin/admin_dashboard.html', {
        'user': user,
        'clinic': clinic,
        'doctors': doctors,
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'cancelled_appointments': cancelled_appointments,
        'confirmed_appointments': confirmed_appointments,
        'total_messages': messages,
    })

# List all contacts
@login_required(login_url='/login/admin/')
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'Admin/contact_list.html', {'contacts': contacts})

# Reply to a contact
@login_required(login_url='/login/admin/')
def reply_contact(request, contact_id):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, id=contact_id)
        data = json.loads(request.body)
        reply_message = data.get('reply_message')

        if not reply_message:
            return JsonResponse({'status': 'error', 'message': 'Reply message cannot be empty.'})

        html_message = render_to_string('emails/reply_email_template.html', {
            'name': contact.name,
            'original_message': contact.message,
            'admin_reply': reply_message,
            'year': datetime.now().year,
        })
        plain_message = strip_tags(html_message)
        
        # Send the reply email
        try:
            if send_mail(
                subject='Response from Polyclinique Tereziya',
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact.email],
                html_message=html_message,
            ):
                contact.is_replied = True
                contact.save()
                
                return JsonResponse({"status": 'success', "message": 'Reply sent successfully!'})
        except Exception as e:
            return JsonResponse({"status": 'error', "message": f'Failed to send reply: {str(e)}'})
    
    return JsonResponse({"status": 'error', "message": 'Invalid request method.'})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            data = {
                'id': user.pk,
                'email': user.email,
                'username': user.username,
                'full_name': user.get_full_name(),
                'last_name': user.last_name,
                'phone_number': user.phone_number,
                'address': user.address,
                'is_patient': user.is_patient,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S'),
                'next': next_url
            }
            return JsonResponse({"status": 'success', "message": 'Logged in successfully.', "data": data})
        else:
            return JsonResponse({'status': 'error', "message": "Invalid email or password"})
    
    return render(request, 'Account/login_admin.html')

def login_patient_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            
            data = {
                'id': user.pk,
                'email': user.email,
                'username': user.username,
                'full_name': user.get_full_name(),
                'last_name': user.last_name,
                'phone_number': user.phone_number,
                'address': user.address,
                'is_patient': user.is_patient,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S'),
                'next': next_url
            }
            return JsonResponse({"status": 'success', "message": 'Logged in successfully.', "data": data})
        else:
            return JsonResponse({'status': 'error', "message": "Invalid email or password"})
    
    return render(request, 'Account/login_patient.html')

def register_patient_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('')
        
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', "message": "Email already exists."})
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', "message": "Username already exists."})
        if CustomUser.objects.filter(username=username, password=password).exists():
            return JsonResponse({'status': 'error', "message": "Account with those credentials already exists"})
        
        user = CustomUser.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            is_patient=True,
        )
        try:
            user.set_password(password)
            user.save()
            return JsonResponse({'status': 'success', "message": "Registration successful! Please log in."})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to register: {str(e)}"})
    return render(request, 'Account/register_patient.html')

def register_admin_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('')
        
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', "message": "Email already exists."})
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', "message": "Username already exists."})
        if CustomUser.objects.filter(username=username, password=password).exists():
            return JsonResponse({'status': 'error', "message": "Account with those credentials already exists"})
        
        user = CustomUser.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            is_patient=False,
            is_superuser=True,
            is_staff=True,
        )
        try:
            user.set_password(password)
            user.save()
            return JsonResponse({'status': 'success', "message": "Registration successful! Please log in."})
        except Exception as e:
            return JsonResponse({'status': 'error', "message": f"Failed to register: {str(e)}"})
    return render(request, 'Account/register_admin.html')

@login_required(login_url='/patient/login/')
def account_details_view(request):
    return render(request, 'Account/patient_account.html', {'user': request.user})

@login_required(login_url='/login/admin/')
def admin_account_details_view(request):
    return render(request, 'Account/admin_account.html', {'user': request.user})

@login_required(login_url='/patient/login/')
def update_patient_view(request):
    if request.method == 'POST':
        user = request.user
        form = UpdatePatientForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account updated successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to update account. Please check the fields.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@login_required(login_url='/login/admin/')
def update_admin_view(request):
    if request.method == 'POST':
        user = request.user
        form = UpdatePatientForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account updated successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to update account. Please check the fields.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"status": 'success', 'message': "You have been logged out successfully."})
    return JsonResponse({"status": 'error', 'message': "You are not logged in."})

