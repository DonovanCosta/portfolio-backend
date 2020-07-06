from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Biography)
admin.site.register(models.Technologies)
admin.site.register(models.Projects)
