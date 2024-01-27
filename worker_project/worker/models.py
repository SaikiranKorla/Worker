from django.db import models

# Create your models here.
# worker/models.py
from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # Adjust length as needed
    address = models.TextField()
    email = models.EmailField()
    key_skills = models.TextField()
    availability = models.TextField()  # You might want to use a better field type

    def __str__(self):
        return self.name
