from __future__ import unicode_literals
from ..login.models import User
from django.contrib import messages

from django.db import models

# Create your models here.

class WishlistManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['name']) == 0:
            errors.append("Cannot be blank.")
        if len(postData['name']) < 3:
            errors.append("Must be more than 3 characters")
        return errors

class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    added_by = models.ManyToManyField(User)
    objects = WishlistManager()
