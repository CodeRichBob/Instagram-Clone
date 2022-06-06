from django.shortcuts import render, redirect
from .models import Post, Profile,
from django.utils import timezone
from datetime import datetime

# Create your views here.

def post(request):
    posts = Post.objects.all().filter(created_date__lte = timezone.now()).order_by('-created_date')


    return render(request, 'insta/post.html', {'posts':posts})

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



    return render(request, 'insta/profile.html', {'p_form':p_form,"posts" : posts,'user' : user})  