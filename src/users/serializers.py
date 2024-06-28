from rest_framework import serializers

from users import models


class User(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'last_name', 'first_name', 'patronymic')


class CreateUser(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ('username', 'password', 'password_confirmation')

    def validate(self, attrs: dict) -> dict:
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError('Введенные пароли не совпадают!')
        attrs.pop('password_confirmation')

        return attrs
