from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    university_name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.university_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ManyToManyField(University)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teachers(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    university = models.ManyToManyField(University)
    name = models.CharField(max_length=150, db_index=True)
    surname = models.CharField(max_length=150, db_index=True)
    birthday = models.DateField(auto_now=False)
    specialty = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Students(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
        (3, 'Archived'),
    )
    university = models.ManyToManyField(University)
    name = models.CharField(max_length=150, db_index=True)
    surname = models.CharField(max_length=150, db_index=True)
    birthday = models.DateField(auto_now=False)
    specialty = models.CharField(max_length=150, db_index=True)
    course = models.IntegerField(default=1, choices = STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




