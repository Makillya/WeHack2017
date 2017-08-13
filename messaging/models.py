# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from loginreg.models import User

class MessageManager(models.Manager):
    def test(self):
        pass

class Message(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    addressee = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = MessageManager()