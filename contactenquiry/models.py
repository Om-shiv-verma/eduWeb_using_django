from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
