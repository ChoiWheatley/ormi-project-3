import decimal
from django.db import models
from users.models import Member


class ChatBot(models.Model):
    timestamp = models.TimeField(auto_now_add=True)
    member = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, default="gpt-3.5-turbo")
    temperature = models.DecimalField(max_digits=5, decimal_places=4, default=decimal.Decimal(1.0))
    stream = models.BooleanField(default=False)
    max_tokens = models.PositiveIntegerField(default=4096)


class Prompt(models.Model):
    prompt = models.CharField(max_length=2047)
    answer = models.TextField(blank=True)

    chatbot = models.ForeignKey(to=ChatBot, on_delete=models.CASCADE)


class ChatBotReply(models.Model):
    prompt_token_usage = models.PositiveIntegerField()
    completion_token_usage = models.PositiveIntegerField()

    chatbot = models.ForeignKey(to=ChatBot, on_delete=models.CASCADE)

    def total_token_usage(self) -> int:
        return self.prompt_token_usage + self.completion_token_usage


class Choice(models.Model):
    """ref: https://platform.openai.com/docs/api-reference/making-requests"""

    role = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    finish_reason = models.CharField(max_length=255)
    index = models.PositiveIntegerField()

    reply = models.ForeignKey(to=ChatBotReply, on_delete=models.CASCADE)
