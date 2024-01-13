from rest_framework.permissions import BasePermission
from .models import Profile, User


class IsUser(BasePermission):
    def has_permissio(self, request, veiw):
        try:
            return request.user
        except User.DoesNotExist:
            return False

    def has_object_permission(self, request, veiw):
        # if request.method == 'DELETE' and obj.user.profile.is_student:
        #     return False
        # elif request.method == 'DELETE' and obj.user.profile.is_teacher:
        #     return True
        
        return True


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.profile.is_admin
        except User.DoesNotExist:
            return False

    def has_object_permission(self, request, view, obj):
        return True
        

        

