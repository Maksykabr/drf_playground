from django.db import models

class University(models.Model):
    university_name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.university_name

class Teachers(models.Model):
    university = models.ManyToManyField(University)
    name = models.CharField(max_length=150, db_index=True)
    surname = models.CharField(max_length=150, db_index=True)
    birthday = models.DateField(auto_now=False)
    specialty = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Students(models.Model):
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
