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
    specialty = models.CharField(max_length=150, db_index=True)
    def __str__(self):
        return self.user
        


