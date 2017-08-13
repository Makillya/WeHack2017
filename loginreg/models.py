# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def testy(self):
        pass

class RelationshipManager(models.Manager):
    def test(self):
        pass

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5)
    user_type = models.CharField(max_length=6)
    skills = models.TextField(blank=True)
    title = models.CharField(max_length=45, blank=True)
    company = models.CharField(max_length=60, blank=True)
    about = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    relationships = models.ManyToManyField("self", through="Relationship",
                                            symmetrical=False,
                                            related_name="related_to+")
    objects = UserManager()
    def __unicode__(self):
        return self.name

RELATIONSHIP_CONNECTED = 1
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_CONNECTED, 'Connected')
)



class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='from_people')
    to_user = models.ForeignKey(User, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
    objects = RelationshipManager()
    