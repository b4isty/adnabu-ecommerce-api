from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import CustomUserModel
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    # confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")

    # def validate(self, data):
    #     """
    #     Check validation for password
    #
    #     """
    #     password = data.get("password")
    #     # confirm_password = data.pop("confirm_password")
    #     if password
    #         return data
    #     return serializers.ValidationError("Password doesn't match")

    def create(self, validated_data):
        # validated_data["password"] = make_password(validated_data.get("password"))
        user = User.objects.create_user(**validated_data)
        validated_data.pop("password")
        return user
