from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    phone_number = models.CharField(
        max_length=12,
        null=True,
        blank=True
    )

    addess = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    email = models.EmailField(
        unique=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.email
    
    
class Profile(models.Model):

    STATUS_CHOICE = [
        ('he/him', 'HE/HIM'),
        ('she/her', 'SHE/HER')
    ]

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        max_length=30,
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True
    )

    profile_pic = models.ImageField(
        upload_to='images/users_profile_pic',
        null=True,
        blank=True
    )

    single_status = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    pronounse = models.CharField(
        choices=STATUS_CHOICE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username