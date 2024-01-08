from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication

from .models import University, Teachers, Students, Profile
from .serializers import UniversitySerializer, TeachersSerializer, StudentsSerializer, ProfileSerializer
from .permissions import IsStudent, IsTeacher, IsAdmin, IsUser, NewUser


class UniversityViewsSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (IsUser, IsStudent, IsTeacher, IsAdmin)
    


class TeachersViewsSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = (IsUser, IsStudent, IsTeacher, IsAdmin)


class StudentsViewsSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsUser, IsStudent, IsTeacher, IsAdmin)

class ProfileCreateUserView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_class = (NewUser,)
    # pagination_class = None
    authentication_classes = (SessionAuthentication,)
    # pagination_class = (NewUser,)



class ProfileViewsSet(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsUser, IsStudent, IsTeacher, IsAdmin)