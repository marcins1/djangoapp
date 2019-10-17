from django.contrib import admin
# Register your models here.
from pizza import models
admin.site.register(models.Pizza)
admin.site.register(models.Skladnik)