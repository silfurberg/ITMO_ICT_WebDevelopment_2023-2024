from django.contrib import admin
from homework import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.StudentHomework)
admin.site.register(models.Subject)
admin.site.register(models.Homework)