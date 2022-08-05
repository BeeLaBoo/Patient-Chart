from django import  forms
from django.forms import ModelForm
from clinicalsApp.models import Patient, ClinicalData

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields = '__all__'