# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Mentor, Mentee

admin.site.register(Mentor)
admin.site.register(Mentee)

# Register your models here.
