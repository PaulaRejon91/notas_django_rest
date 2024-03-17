from django.db import models


# Model for the notes
class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
# This is the string representation of the object
    def __str__(self):
        return self.title