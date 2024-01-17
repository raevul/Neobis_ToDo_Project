from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField("Complete", default=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.TimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
