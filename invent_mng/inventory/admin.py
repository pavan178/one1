from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


# Register your models here.


# Register your models here.

@admin.register(Item1, Item2, Item3)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)
