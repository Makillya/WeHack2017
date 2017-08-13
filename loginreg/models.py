# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import bcrypt
import re
from datetime import date, datetime, timedelta, time
import datetime

# Matches the email to make sure the format is atleast one letter (lower or uppercase),
# number, or of of there characters . + _ -  Then an @ sign with the same format and
# lastly make sure there is a . followed by the same pattern.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# The password is any characters and there are atleast 7.
PASSWORD_REGEX = re.compile(r'^.{7,}$')

# The username checks for numbers and letters that can contain _ or . just not next to
# eachother, plus there has to be 5 through 18 characters.
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){5,18}[a-zA-Z0-9]$')

# The date just checks for a year with 4 numbers a month with 2 numbers and a day with 2
# numbers.
DATE_REGEX = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$')

class mentorManager(models.Manager):
    # Call this function to check for validation of all field for registation.
    # How to call: Table.userManager.registration(request.POST)
    def registerMentor(self, userInput):
        # errorList - Keeps tracks of all errors with the validation.
        errorList = []

        # Checks to see if first_name is greater than 2 characters.
        if len(userInput['first_name']) < 2:
            errorList.append('First name needs to be greater than 2 letters!\n')

        # Checks to see if last_name is greater than 2 characters.
        if len(userInput['last_name']) < 2:
            errorList.append('Last name needs to be greater than 2 letters!\n')

        # Checks to see if first_name contains only alphabetical letters.
        if not userInput['first_name'].isalpha():
            errorList.append('First name may only contain letters!\n')

        # Checks to see if last_name contains only alphabetical letters.
        if not userInput['last_name'].isalpha():
            errorList.append('Last name may only contain letters!\n')

        # Checks if the email matches the EMAIL_REGEX.
        if not EMAIL_REGEX.match(userInput['email']):
            errorList.append('Email is not a valid email! Try this format: something@example.com\n')

        # Checks if the password matches the PASSWORD_REGEX.
        if not PASSWORD_REGEX.match(userInput['password']):
            errorList.append('Password is not long enough.\n')

        # Checks to make sure the password inputs match.
        if userInput['password'] != userInput['confirm_password']:
            errorList.append('Password match not confirmed.\n')

        # Checks the database to see if the email already exists.
        if self.filter(email = userInput['email']):
            errorList.append('This email already exists in our database.\n')

        # If the list has no errors.
        if not errorList:
            hashed = bcrypt.hashpw(userInput['password'].encode(), bcrypt.gensalt())
            current_user = self.create(first_name = userInput['first_name'], last_name = userInput['last_name'], email = userInput['email'], password = hashed)
            return True, current_user
        return False, errorList

    # Call this function to check for validation of all field for login.
    # How to call: Table.userManager.login(request.POST)
    def login(self, userInput):
        # errorList - Keeps tracks of all errors with the validation.
        errorList = []

        # Checks if the email and password don't match.
        if not userInput['email'] and not userInput['password']:
            errorList.append('Unsuccessful login. Please fill in the email and password field!\n')
            return False, errorList
        # Check if user is in Mentor table
        elif self.filter(email = userInput['email']) :
            hashed = self.get(email = userInput['username_email']).password.encode()
            password = userInput['password'].encode()
            # Check to see if user is in Mentee table
        elif Mentee.menteeManager.filter(email = userInput['email']):
            hashed = Mentor.mentorManager.get(email = userInput['email']).password.encode()
            password = userInput['password'].encode()

            # Checks if the password is the correct one to the hashed one.
            if bcrypt.hashpw(password, hashed) == hashed:
                return True, self.get(email=userInput['email'])

            else:
                errorList.append('Unsuccessful login. Incorrect password!\n')
        else:
            errorList.append('Unsuccessful login. Your email or username is incorrect!\n')
        return False, errorList


class menteeManager(models.Manager):
    # Call this function to check for validation of all field for registation.
    # How to call: Table.userManager.registration(request.POST)
    def registerMentee(self, userInput):
        # errorList - Keeps tracks of all errors with the validation.
        errorList = []

        # Checks to see if first_name is greater than 2 characters.
        if len(userInput['first_name']) < 2:
            errorList.append('First name needs to be greater than 2 letters!\n')

        # Checks to see if last_name is greater than 2 characters.
        if len(userInput['last_name']) < 2:
            errorList.append('Last name needs to be greater than 2 letters!\n')

        # Checks to see if first_name contains only alphabetical letters.
        if not userInput['first_name'].isalpha():
            errorList.append('First name may only contain letters!\n')

        # Checks to see if last_name contains only alphabetical letters.
        if not userInput['last_name'].isalpha():
            errorList.append('Last name may only contain letters!\n')

        # Checks if the email matches the EMAIL_REGEX.
        if not EMAIL_REGEX.match(userInput['email']):
            errorList.append('Email is not a valid email! Try this format: something@example.com\n')

        # Checks if the password matches the PASSWORD_REGEX.
        if not PASSWORD_REGEX.match(userInput['password']):
            errorList.append('Password is not long enough.\n')

        # Checks to make sure the password inputs match.
        if userInput['password'] != userInput['confirm_password']:
            errorList.append('Password match not confirmed.\n')

        # Checks the database to see if the email already exists.
        if self.filter(email = userInput['email']):
            errorList.append('This email already exists in our database.\n')

        # If the list has no errors.
        if not errorList:
            hashed = bcrypt.hashpw(userInput['password'].encode(), bcrypt.gensalt())
            current_user = self.create(first_name = userInput['first_name'], last_name = userInput['last_name'], email = userInput['email'], password = hashed)
            return True, current_user
        return False, errorList











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
    
