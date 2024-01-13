from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status

from .permissions import IsAdmin, IsUser
from .models import University, Profile, User
from .serializers import UniversitySerializer, ProfileSerializer, UserSerializer
# from .permissions import IsStudent, IsTeacher, IsAdmin, IsUser, NewUser


class UniversityViewsSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    authentication_classes = [SessionAuthentication]


class ProfilesViewsSet(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    authentication_classes = [SessionAuthentication]

class UsersViewsSet(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    authentication_classes = [SessionAuthentication]


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = (AllowAny,)
    # authentication_classes = [SessionAuthentication]


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Perform authentication (e.g., using Django's built-in authenticate() function)
        user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful!'}, status=200)
        else:
            return Response({'message': 'Invalid credentials'}, status=400)
    permission_class = (AllowAny,)

# class UserCreateView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)