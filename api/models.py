from django.db import models
import uuid

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=500, db_index=True)
    content = models.TextField()
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    alias = models.CharField(max_length=200)
    hashed_unlock_key = models.TextField()
    is_published = models.BooleanField(default=False, db_index=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['alias', 'hashed_unlock_key'])
        ]



