from django.contrib import admin
from .models import University, Teachers, Students, Profile


# admin.site.register(University)
# admin.site.register(Teachers)
# admin.site.register(Students)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = []


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = []