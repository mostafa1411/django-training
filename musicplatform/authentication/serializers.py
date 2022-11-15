from rest_framework import serializers
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password1', 'password2']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password1'])
        return user

    def validate(self, attrs):
        users = User.objects.all()

        for user in users:
            if user.username == attrs.get('username'):
                raise serializers.ValidationError('The username is used by another user')
            if user.email == attrs.get('email'):
                raise serializers.ValidationError('The email is used by another user')

        if attrs.get('password1') != attrs.get('password2'):
            raise serializers.ValidationError('The passwords does not match.')

        return attrs
