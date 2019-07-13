from django.contrib import admin
from . import models

admin.site.register(models.CSVFile)
admin.site.register(models.ParsedCSV)
