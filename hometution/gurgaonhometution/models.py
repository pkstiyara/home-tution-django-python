from django.db import models

# Create your models here.

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    # Add other fields as needed

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()