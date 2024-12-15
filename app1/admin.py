from django.contrib import admin # type: ignore
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmploeeAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","DOB","gender","skills","County","Residence","profile_pic","resume","video")
