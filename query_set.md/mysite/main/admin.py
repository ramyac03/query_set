from django.contrib import admin
from .models import Define,Info,Student ,Blog,Entry,Author#we have to import the models for database in admin site

# Register your models here.
admin.site.register(Define)
admin.site.register(Info)
admin.site.register(Student)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
#  register the site
