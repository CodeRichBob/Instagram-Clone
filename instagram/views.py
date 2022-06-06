from django.shortcuts import render, redirect
from .models import Post, Profile, Likes, Comment 
from django.utils import timezone
from .forms import ProfileUpdateForm,CommentForm,PostForm
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


def new_comment(request,pk):
    post = Post.objects.get(pk = pk)

    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.user.username
            comment= form.cleaned_data['comment']
            obj = Comment(post = post,name = name,comment = comment,date = datetime.now())
            obj.save()
        return redirect('post')
    else:
        form = CommentForm()

    return render(request, 'instagram/comment.html', {"form": form})   

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # We pass in the request.FILES argument because we are going to be uploading an Image file and we want to process that in our form.
        if form.is_valid():
            post = form.save(commit = False)
            post.author = current_user
            post.save()
        return redirect('post')
    else:
        form = PostForm()
    return render(request, 'instagram/create_post.html', {"form": form}) 


def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_articles = Post.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'instagram/search.html',{"message":message,"photos": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagram/search.html',{"message":message})   


def delete_post(request,pk): 
    post = Post.objects.get(pk = pk)
    if request.method == 'POST':
        post.delete()

        return redirect('post')

    return render(request, 'instagram/delete_post.html',{})

def update_post(request,pk):
    post = Post.objects.get(id = pk)
    form = PostForm(instance = post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance = post)
        # We pass in the request.FILES argument because we are going to be uploading an Image file and we want to process that in our form.
        if form.is_valid():
            post.save()
        return redirect('post')
   

    return render(request, 'instagram/update_post.html',{'form' :form})   