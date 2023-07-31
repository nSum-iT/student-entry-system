from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    grade = models.CharField(max_length=5)
    major = models.CharField(max_length=20)

    def __str__(self):
        return self.name