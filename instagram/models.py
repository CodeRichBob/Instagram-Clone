from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_image = CloudinaryField('image', null = True, default = 'default.jpg')
    bio = models.TextField(default='')
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
