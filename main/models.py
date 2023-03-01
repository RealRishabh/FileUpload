from django.db import models
from datetime import datetime

# Create your models here.
class FileTable(models.Model):
    file = models.FileField(blank=False, null=False)
    created_at = models.DateTimeField(default=datetime.now)