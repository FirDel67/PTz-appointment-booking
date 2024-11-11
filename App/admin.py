from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Availability)
admin.site.register(Appointment)