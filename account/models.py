from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_of_birth = models.DateTimeField(blank=True, null=True,verbose_name='Date of birth')
    photo = models.ImageField(upload_to='users/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

