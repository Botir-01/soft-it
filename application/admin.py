from django.contrib import admin
from .models import CustomerApplication, CustomerProjectApplication

# Register your models here.
admin.site.register(CustomerApplication)
admin.site.register(CustomerProjectApplication)