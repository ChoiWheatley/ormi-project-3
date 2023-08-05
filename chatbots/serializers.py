from rest_framework.serializers import ModelSerializer
from chatbots.models import ChatBot


class ChatBotSerializer(ModelSerializer):
    class Meta:
        model = ChatBot
        fields = "__all__"

    def create(self, validated_data):
        # TODO - impl
        pass
