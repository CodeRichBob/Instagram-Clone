from django.shortcuts import render, redirect
from .models import Post, Profile
from django.utils import timezone
from datetime import datetime

# Create your views here.

def post(request):
    posts = Post.objects.all().filter(created_date__lte = timezone.now()).order_by('-created_date')


    return render(request, 'instagram/post.html', {'posts':posts})

def profile(request):
    user = Profile.objects.get_or_create(user=request.user)
    user = request.user
 
    posts = Post.objects.filter(author=request.user).order_by('-created_date')

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)

        if p_form.is_valid():
            p_form.save()
            # messages.success(request,f'your account has been updated')

            return redirect('profile')


    else:
        p_form = ProfileUpdateForm(instance = request.user.profile)



    return render(request, 'instagram/profile.html', {'p_form':p_form,"posts" : posts,'user' : user}) 


def like(request,post_id):
    user = request.user
    post = Post.objects.get(id = post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user = user,post = post).count()
    if not liked:
        Likes.objects.create(user = user,post = post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user = user,post = post).delete()  
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return redirect('post') 