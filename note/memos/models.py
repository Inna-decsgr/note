from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_bookmark = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.title
