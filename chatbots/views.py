from chatbots.models import ChatBot, ChatBotReply, Prompt, Choice
from django.core.exceptions import PermissionDenied
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

authenticator = JWTAuthentication()


class ChatBotViewSet(ViewSet):
    """
    focused on individual, api for controlling usecases specified below:

    - retrieve personal chat history, prompts and replies can be null
    - create new chat
    - update select chat
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        auth = authenticator.authenticate(request)
        if auth is None:
            raise PermissionDenied()

        user, token = auth
        chats = ChatBot.objects.filter(member_id=user.id)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass
