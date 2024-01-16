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

    

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     isinstance = self.Meta.model(**validated_data)
    #     instance.is_active = True
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['user', 'password', 'university', 'is_teacher', 'is_student', 'specialty']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user