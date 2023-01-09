from distutils.command.upload import upload
from email.mime import image
from tokenize import blank_re
from django.db import models


class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)


class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

class client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)
