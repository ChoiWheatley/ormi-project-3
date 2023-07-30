from django.contrib import admin
from .models import *


admin.site.register(ChatBot)
admin.site.register(Prompt)
admin.site.register(ChatBotConfig)
admin.site.register(ChatBotReply)
admin.site.register(Choice)
