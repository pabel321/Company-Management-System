from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.TextField(max_length=100, blank=False)
    subject = models.TextField(max_length=200, blank=False)
    message = models.TextField(max_length=700, blank=False)
    
