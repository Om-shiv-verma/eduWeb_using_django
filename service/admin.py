from django.contrib import admin
from service.models import Service
from service.models import Contact_img
#import Service class from models.py jo secvice folder me hai

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')

admin.site.register(Service,ServiceAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('vision','imgpath')

admin.site.register(Contact_img,ServiceAdmin)

# Register your models here.
