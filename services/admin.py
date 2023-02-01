from django.contrib import admin
from .models import Services
# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')    #readonly_fields es una tupla para mostar los campo solo de lectura

admin.site.register(Services, ServicesAdmin)