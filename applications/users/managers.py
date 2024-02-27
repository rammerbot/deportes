from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, name, last_name,email, password, is_staff, is_superuser, **extra_fields): 
        user = self.model(
            username = username,
            name = name,
            last_name = last_name,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name, last_name, email, password, **extra_fields):
        return self._create_user(username, name, last_name, email,  password, False, False, **extra_fields)
    
    def create_superuser(self, username, name, last_name, email, password=None, **extra_fields):
        return self._create_user(username, name, last_name, email,  password, True, True, **extra_fields)