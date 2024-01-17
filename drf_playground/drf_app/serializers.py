from rest_framework import serializers
from .models import University, Profile, User
from django.contrib.auth.hashers import make_password


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:

        return make_password(value)


    class Meta:
        model = User
        fields = '__all__'

    

