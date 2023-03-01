from django.contrib import admin
from .models import FileTable

# Register your models here.
@admin.register(FileTable)
class FileTableAdmin(admin.ModelAdmin):
    list_display = ('file', 'created_at')