
import datetime
from django.conf import settings
from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    createdAt = models.DateField(("Date"), default=datetime.date.today)
    checked = models.BooleanField(default=False)
    
