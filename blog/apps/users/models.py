from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from cloudinary.models import CloudinaryField

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    about = models.TextField(blank=True, null=True)
    avatar = CloudinaryField(null=True, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} | {self.first_name} + {self.last_name}'
    
    @property
    def avatar_url(self):
        if self.avatar == None:
            return ("null")
        else:
            return(
                f"https://res.cloudinary.com/dey5v9yb0/{self.avatar}"
            )
    
    class Meta:
        ordering = ["date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"
    