from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email')



class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True,
                                    label='Password', style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, 
                                    label='Confirm Password',style={'input_type': 'password'})


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        
        user = User(username=username, email=email)

        if password != validated_data['password2']:
            raise ValidationError('Passwords not match')
        else:
            user.set_password(password)
            user.save()
        return validated_data