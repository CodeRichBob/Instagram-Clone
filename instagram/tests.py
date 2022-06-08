from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post,Likes,Comment

# Create your tests here.  

class PostTestClass(TestCase):
    def setUp(self):
        user = User.objects.create()
        self.new_image = Post(likes = '5',author = user,caption = 'test_caption',location = 'test_location',created_date = '2021-10-04' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Post))   

    def test_save_method(self):
            self.new_image.save_image()
            images = Post.objects.all()
            self.assertTrue(len(images) > 0)   

    def tearDown(self):
            Post.objects.all().delete()
            Comment.objects.all().delete()
            Likes.objects.all().delete()

    def test_delete_method(self):
            self.new_image.save_image()
            self.new_image.delete_image()
            images = Post.objects.all()
            self.assertTrue(len(images) == 0)     

    def test_update_method(self):
            self.new_image.save_image()
            self.new_image.update_caption()
            images = Post.objects.all()
            self.assertTrue(len(images) > 0) 