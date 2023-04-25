from django.contrib import admin
from contactenquiry.models import contactEnquiry
#import Service class from models.py jo secvice folder me hai

class save(admin.ModelAdmin):
    list_display = ('fname','lname','fathername','email','phone')

admin.site.register(contactEnquiry,save)

# Register your models here.
