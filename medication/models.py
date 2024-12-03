from django.db import models
from authentication.models import RoleBasedUser

# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=30)
    instructions = models.TextField(max_length=300)
    
    def __str__(self):
        return f"{self.name} {self.instructions[0:15]}"

class Prescription(models.Model):
    PERIOD_CHOICES = (
        ("M", "Morning"),
        ("A", "Afternoon"),
        ("E", "Evening")
    )

    period = models.CharField(choices=PERIOD_CHOICES, max_length=1)
    isAfterFood = models.BooleanField(default = True)
    duration = models.IntegerField()

    # fks
    doctor = models.ForeignKey(RoleBasedUser, on_delete=models.CASCADE, related_name="author")
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    patient = models.ForeignKey(RoleBasedUser, on_delete=models.CASCADE, related_name="target")

    def __str__(self):
        return f"{self.patient} {self.period}"

class Intake(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, default=-1)
    date = models.DateField(auto_now_add=True)
    period = models.CharField(choices=Prescription.PERIOD_CHOICES, max_length=1, default='M') # at which the medication was actually taken0

    def __str__(self):
        return f"{self.date} {self.period}"