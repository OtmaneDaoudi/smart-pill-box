from django.forms import ModelForm
from .models import Medication

class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ["name", "instructions"]