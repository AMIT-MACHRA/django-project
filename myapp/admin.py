from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(contact)

class orderAdmin(admin.ModelAdmin):
    list_display = ('FirstName','LastName','Gender','Email','PhoneNumber','address','order')
admin.site.register(login,orderAdmin)
admin.site.register(blogs)