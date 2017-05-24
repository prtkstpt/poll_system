from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    username = models.CharField(max_length=100)
    roll_no = models.PositiveIntegerField()
    course = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Candidate(models.Model):
    student = models.OneToOneField(Student)
#    user = models.ForeignKey(User)
    symbol = models.CharField(max_length=100)
    vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.symbol
