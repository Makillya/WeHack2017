# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Mentor(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5)
    skills = models.TextField(blank=True)
    title = models.CharField(max_length=45, blank=True)
    company = models.CharField(max_length=60, blank=True)
    about = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Mentee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5)
    skills = models.TextField(blank=True)
    title = models.CharField(max_length=45, blank=True)
    company = models.CharField(max_length=60, blank=True)
    about = models.TextField(blank=True)
    teacher = models.ManyToManyField(Mentor, related_name="student")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



