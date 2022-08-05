from django.contrib import admin
from .models import  Patient,ClinicalData
# Register your models here.
admin.site.register(Patient)
admin.site.register(ClinicalData)