from django.contrib import admin
from .models import Define,Info #we have to import the models for database in admin site

# Register your models here.
admin.site.register(Define)
admin.site.register(Info)
#  register the site
