import uuid
from django.db import models

class APIKey(models.Model):
    key = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
