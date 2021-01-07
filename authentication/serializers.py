
from rest_framework import serializers
from .models import User 
from django.contrib.auth.password_validation import validate_password

class LoginSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['phone', 'password']


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'password_2',)
        extra_kwargs = {
            'phone': {'required': True},
            'password': {'required': True},
            'password2': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            phone=validated_data['phone'],
            password=validated_data['password'],
            password_2=validated_data['password_2']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user