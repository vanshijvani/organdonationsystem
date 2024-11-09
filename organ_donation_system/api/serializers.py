from rest_framework import serializers
from django.contrib.auth.models import User
from .models import donors
from .models import recipients

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = recipients
        fields ='__all__'
        

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = donors
        fields = '__all__'
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # Create a new user and hash the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

