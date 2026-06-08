from rest_framework import serializers
from .models import Usersm, Appointment, PatientRecord, Speciality, Clinic, Analysis, Notificatios


class Usermserializers(serializers.ModelSerializer):
    class Meta:
        model = Usersm
        fields = ("name", "email", "phone", "password", "id", "type",)

class Appointmentserializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("date", "time", "state", "doctor", "patient", "id")

class PatientRecordserializers(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = ("diagnose", "id", "doctor", "patient", "notes", "nextappointment", "mediicines", "age", "gender", )

class Specialityserializers(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ("name", "id",)

class Clinicserializers(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ("doctor", "name", "speciality", "id", )

class Analysisserializers(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ("doctor", "patient", "type", "img","id", )

class Notificatiosserializers(serializers.ModelSerializer):
    class Meta:
        model = Notificatios
        fields = ("from_user", "to_user", "time", "state","id","text" ,"analysis" ,"appointment" ,)