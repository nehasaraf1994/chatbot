from django.contrib import admin

# Register your models here.
from .models import Typo, Doctor

admin.site.register(Typo)
admin.site.register(Doctor)
