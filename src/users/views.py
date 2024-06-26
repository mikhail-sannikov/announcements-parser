from djoser.views import UserViewSet

from users import serializers


class User(UserViewSet):
    def get_serializer_class(self) -> serializers:
        serializer_class = super().get_serializer_class()

        if self.action == 'create':
            serializer_class = serializers.CreateUser

        return serializer_class
