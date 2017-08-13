# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from loginreg.models import User

class MessageManager(models.Manager):
    # Add message function
    def add(self, userInput, creatorId, addresseeId):
        errors=[]
        # VALIDATION FOR MESSAGE
        if len(userInput["content"]<1):
            errors.append("Please add a message!")
        if not creatorId:
            errors.append("Can't find craetorId!")
        if not addresseeId:
            errors.append("Cant't find addresseeId!")
        if not errors:
            current_message=self.create(content=userInput["content"], creator=creatorId, addressee=addresseeId)
            return True, current_message
        return False, errors


class Message(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_message")
    addressee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addressee_message")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = MessageManager()
