from django.contrib import admin

# Register your models here.

from chats.models import Message,Conversation
admin.site.register(Message)
admin.site.register(Conversation)