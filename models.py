from django.db import models

# Create your models here.

class Usersm(models.Model):
    name = models.fields.CharField(max_length=100,unique=True)
    email = models.fields.EmailField()
    phone = models.fields.CharField(max_length=50)
    password = models.fields.CharField(max_length=200)
    TYPE_CHOICES = (
        ('DOCTOR', 'Doctor'),
        ('PATIENT', 'Patient'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=25, blank=True, default='PATIENT')

    def __str__(self):
        return f"{self.name}"

class Appointment(models.Model):
    date = models.fields.DateField()
    time = models.fields.TimeField()
    STATE_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELED', 'Canceled'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=25, blank=True, default='PENDING')
    doctor = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name='my_doctor')
    patient = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name='my_patient')
    def __str__(self):
        return f"{self.doctor.name} {self.patient.name}"

class PatientRecord(models.Model):
    diagnose = models.fields.CharField(max_length=2000)
    doctor = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name='doctors')
    patient = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name='patients')
    notes = models.fields.CharField(max_length=2000)
    nextappointment = models.fields.CharField(max_length=100)
    mediicines = models.fields.CharField(max_length=1000)
    age = models.fields.IntegerField()
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25, blank=True, default='MALE')


class Speciality(models.Model):
    name = models.fields.CharField(max_length=2000)
    def __str__(self):
        return f"{self.name}"

class Clinic(models.Model):
    doctor = models.ForeignKey(Usersm, on_delete=models.CASCADE)
    name = models.fields.CharField(max_length=2000)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"


class Analysis(models.Model):
    doctor = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name='mydoctor')
    patient = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name='mypatient')
    type = models.fields.CharField(max_length=2000)
    img = models.ImageField()

class Notificatios(models.Model):
    from_user = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name="from_users")
    to_user = models.ForeignKey(Usersm, on_delete=models.CASCADE, related_name="to_users")
    time = models.fields.DateTimeField(auto_now_add=True)
    state = models.fields.BinaryField()
    text = models.fields.CharField(max_length=2000)
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE,blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,blank=True)





