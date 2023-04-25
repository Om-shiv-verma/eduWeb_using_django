from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()

class Contact_img(models.Model):
    vision = models.CharField(max_length=500)
    imgpath = models.CharField(max_length=50)