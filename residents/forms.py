from django import forms
from .models import Resident

class ResidentForm(forms.ModelForm):

    class Meta:
        model = Resident
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "nationality",
            "phone",
            "emergency_contact",
            "emergency_phone",
            "admission_date",
            "allergies",
            "diseases",
            "treatments",
            "medical_notes",
            "observations",
            "status",
            "room",
            "photo",
        ]