from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser
from .models import Profile

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        # if request.user.profile.is_student:
        #     True
        # else:
        #     return False
        # try:
        #     return request.user.profile.is_student
        # except Profile.DoesNotExist:
        #     return False
        if isinstance(request.user, AnonymousUser):
            return False
        try:
            return request.user.profile.is_student
        except Profile.DoesNotExist:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and obj.user.profile.is_teacher:
            return False
        elif request.method == 'DELETE' and obj.user.profile.University:
            return False
        else:
            return obj.user == request.user

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.profile.is_teacher
        except Profile.DoesNotExist:
            return False

    def has_object_permission(self, request, view, obj):
        # Teachers can't delete students
        if request.method == 'DELETE' and obj.user.profile.is_student:
            return False
        return True

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.profile.is_admin
        except Profile.DoesNotExist:
            return False

    def has_object_permission(self, request, view, obj):
        return True

class NewUser(BasePermission):
    def has_permission(self, request, view):
        return True