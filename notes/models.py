from django.db import models


# Model for the notes
class Note(models.Model):
    body=models.TextField(null=True, blank=True)
    created=models.DateTimeField(auto_now_Add=True)
    update=models.DateTimeField(auto_now=True)

# String representation of the object
def __str__(self):
     return self.title

#__str__ method to display a readable representation of the Note model instance.