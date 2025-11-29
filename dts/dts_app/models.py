from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    due_date_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
