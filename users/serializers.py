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
        email = validated_data.get("email")
        pw = validated_data.pop("password")

        if Member.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists!")
        
        return Member.objects.create_user(**validated_data, password=pw)