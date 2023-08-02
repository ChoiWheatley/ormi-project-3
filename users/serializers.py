from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        pw = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if pw:
            instance.set_password(pw)
        instance.save()
        return instance


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if not email or password:
            raise serializers.ValidationError("put email and password correctly")
        validate_password(password)
        return attrs
