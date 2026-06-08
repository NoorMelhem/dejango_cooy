from django.shortcuts import render
from .models import Usersm, Appointment, PatientRecord, Speciality, Clinic, Analysis, Notificatios
from .serializers import Usermserializers, Appointmentserializers, PatientRecordserializers, Specialityserializers, Clinicserializers, Analysisserializers, Notificatiosserializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BasicView(APIView):
    def get(self, request, format=None):
        ...
    def post(self, request, format=None):
        ...
    def get_object(self, pk):
        ...
    def put(self, request, pk, format=None):
        ...
    def delete(self, request, pk, format=None):
        ...

class DoctorAPI(BasicView):
    def get(self, request, pk, format=None):
        patients = Usersm.objects.filter(id__in=Appointment.objects.filter(id=pk)).distinct()
        serializer = Usermserializers(patients, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Usermserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return Usersm.objects.get(pk=pk)
        except Usersm.DoesNotExist:
            raise Http404
    
    def get(self, request, myemail, mypassword):
        try:
            
            doctors = Usersm.objects.filter(email = myemail, password = mypassword).distinct()
            serializer = Usermserializers(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usersm.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        userm = self.get_object(pk)
        serializer = Usermserializers(userm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        userm = self.get_object(pk)
        userm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AppointmentAPI(BasicView):
    def get(self, request, pk, tp,  format=None):
        if tp == 1:
            appointment = Appointment.objects.filter(doctor__in=Usersm.objects.filter(id=pk)).distinct()
        else:
             appointment = Appointment.objects.filter(patient__in=Usersm.objects.filter(id=pk)).distinct()
        
        serializer = PatientRecordserializers(appointment, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PatientRecordserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = Appointmentserializers(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PatientRecordAPI(BasicView):
    def get(self, request, pk, tp,  format=None):
        if tp == 1:
            appointment = PatientRecord.objects.filter(doctor__in=Usersm.objects.filter(id=pk)).distinct()
        else:
             appointment = PatientRecord.objects.filter(patient__in=Usersm.objects.filter(id=pk)).distinct()
        
        serializer = PatientRecordserializers(appointment, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PatientRecordserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return PatientRecord.objects.get(pk=pk)
        except PatientRecord.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        patientrecord = self.get_object(pk)
        serializer = PatientRecordserializers(patientrecord, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        patientrecord = self.get_object(pk)
        patientrecord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SpecialityAPI(BasicView):
    def get(self, request, pk, format=None):
        names = Speciality.objects.all()
        serializer = Specialityserializers(names, many=True)
        return Response(serializer.data)
    
class ClinicAPI(BasicView):
    def get(self, request, pk, format=None):
        clinics = Clinic.objects.filter(doctor__in=Usersm.objects.filter(id=pk)).distinct()
        serializer = Clinicserializers(clinics, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Clinicserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, format=None):
        clinic = self.get_object(pk)
        serializer = Clinicserializers(clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        clinic = self.get_object(pk)
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AnalysisAPI(BasicView):
    def get(self, request, pk, format=None):
        analysiss = Analysis.objects.get(pk=pk)
        serializer = Analysisserializers(analysiss, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        analysis = self.get_object(pk)
        serializer = Analysisserializers(analysis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotificatiosAPI(BasicView):
    def get(self, request, pk, format=None):
        notificatios = Notificatios.objects.get(pk=pk)
        serializer = Notificatiosserializers(notificatios, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        notificatios = self.get_object(pk)
        serializer = Notificatiosserializers(notificatios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)