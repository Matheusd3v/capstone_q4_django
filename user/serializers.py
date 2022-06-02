from rest_framework.serializers import ModelSerializer

from user.models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_uuid",
            "username",
            "password",
            "is_superuser",
            "email",
            "first_name",
        )

        extra_kwargs = {
            "user_uuid": {"read_only": True},
            "password": {"write_only": True},
            "is_superuser": {"required": False, "default": False},
        }

    def validate(self, attrs):
        attrs["username"] = attrs["username"].lower()

        return super().validate(attrs)

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)


class UsersDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_uuid",
            "email",
            "first_name",
        )

        extra_kwargs = {"user_uuid": {"read_only": True}}
