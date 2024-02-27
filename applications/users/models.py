from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOISES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    )
    username = models.CharField('Nombre de Usuario', max_length=20, unique=True)
    name = models.CharField('Nombre', max_length=20 )
    last_name = models.CharField('Apellido', max_length=20)
    email = models.EmailField('Correo')
    avatar = models.ImageField('Foto', upload_to="users/", blank=True)
    gender = models.CharField('Genero', max_length=1, choices=(GENDER_CHOISES), blank=True)
    
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['name', 'last_name', 'email']

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f'{self.name} {self.last_name}'
    
