from django.contrib import admin
# Register your models here.
from studenci import models
admin.site.register(models.Uczelnia)
admin.site.register(models.Miasto)
admin.site.register(models.Student)