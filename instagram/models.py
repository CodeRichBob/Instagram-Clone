from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    profile_image = CloudinaryField('image', null = True, default = 'default.jpg')
    bio = models.TextField(default='')
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}Profile'

class Post (models.MOdel):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    location = models.CharField(max_lenth=80, null=True)
