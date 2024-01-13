from django.contrib import admin
from .models import University, Profile


# admin.site.register(University)
# admin.site.register(User)


@admin.register(University)
class ProfileAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Profile)
class UniversityAdmin(admin.ModelAdmin):
    list_display = []

