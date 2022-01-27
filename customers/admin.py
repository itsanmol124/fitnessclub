from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','age','email','number','location']
    search_fields = ["name"]
