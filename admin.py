from django.contrib import admin
from .models import Usersm, Appointment, PatientRecord, Speciality, Clinic, Analysis, Notificatios

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "phone", "type", "id", )
  
admin.site.register(Usersm, UsersAdmin)

class AppointmentAdmin(admin.ModelAdmin):
  list_display = ("date", "time", "state", "doctor", "patient",)
  
admin.site.register(Appointment, AppointmentAdmin)

class SpecialityAdmin(admin.ModelAdmin):
  list_display = ("name",)
  
admin.site.register(Speciality, SpecialityAdmin)

class ClinicAdmin(admin.ModelAdmin):
  list_display = ("doctor", "name", "speciality",)
  
admin.site.register(Clinic, ClinicAdmin)
