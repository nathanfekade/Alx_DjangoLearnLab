from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

 

class UserSerializer(serializers.ModelSerializer):
    following = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'bio', 'profile_picture', 'followers', 'following')
        read_only_fields = ('followers','following')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(
            username= validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
