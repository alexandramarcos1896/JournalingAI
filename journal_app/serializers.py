from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note
from .models import UserProfile

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title', 'content','created_at','user']
        read_only_fields = ['id', 'created_at', 'user'] 
        extra_kwargs = {
            'title': {'required': False},
            'content': {'required': False},
        }

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        UserProfile.objects.create(
            user=user,
            github=profile_data.get('github', ''),
            twitter=profile_data.get('twitter', ''),
            instagram=profile_data.get('instagram', ''),
        )
        return user