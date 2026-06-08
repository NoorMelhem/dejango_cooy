
from django.urls import path, include
from clinic import views


urlpatterns = [
    path('doctor/<int:pk>/', views.DoctorAPI.as_view()),
    path('gdoctor/<str:myemail>/<str:mypassword>/', views.DoctorAPI.as_view()),
    path('appointment/<int:pk>/<int:tp>/', views.AppointmentAPI.as_view()),
    path('patientrecord/<int:pk>/<int:tp>/', views.PatientRecordAPI.as_view()),
    path('speciality/<int:pk>/', views.SpecialityAPI.as_view()),
    path('clinic/<int:pk>/', views.ClinicAPI.as_view()),
    path('analysis/<int:pk>/', views.AnalysisAPI.as_view()),
    path('notificatios/<int:pk>/', views.NotificatiosAPI.as_view()),
]
