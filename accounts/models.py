from django.db import models

# Create your models here.
class Complainant(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

class Officer(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    officer_id = models.CharField(max_length=15)
    email = models.CharField(max_length=50)