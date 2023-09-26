from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conversation(models.Model):
    participants= models.ManyToManyField(User,related_name='conversations')
    latest_message=models.OneToOneField('Message',on_delete=models.SET_NULL,null=True,related_name='lm')
    message_count=models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    notification = models.BooleanField(default=False)

class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=30,)
    conversation= models.ForeignKey(Conversation,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)