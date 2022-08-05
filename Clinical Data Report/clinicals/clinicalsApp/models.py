from django.db import models
from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL

# Create your models here.
class Patient(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    age = models.IntegerField()
    
class ClinicalData(models.Model):
    COMPONENT_NAMES = [('Ht/Wt','Height/Weight'), ('BP','Blood Pressure'),('HR', 'Heart Rate')]
    componentName = models.CharField(choices = COMPONENT_NAMES, max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    Patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    
