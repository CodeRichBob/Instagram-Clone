from django import forms
from .models import Profile,Comment,Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProfileUpdateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Profile','Profile',css_class = 'btn-success  m-2 btn-sm'))

    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'bio',
        ]

class CommentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Comment','Comment',css_class = 'btn-success  m-2 btn-sm'))

    class Meta:
        model = Comment
        fields = [
            'comment',
            
        ]

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post','Post',css_class = 'btn-primary m-2 btn-sm '))

    class Meta:
        model = Post
        fields = [
            'image',
            'caption',
            'location'
        ]