from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import Post,Follow
from django.contrib import messages
from .forms import Create_Post, Edit_Post_Form,Add_Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@login_required
def create_post(request):
    form = Create_Post()
    if request.method == 'POST':
        form = Create_Post(request.POST, request.FILES)
        if form.is_valid():
            postboi = form.save(commit=False)
            postboi.creator = request.user
            postboi.save()
            messages.success(request, 'POST CREATED')
            return HttpResponseRedirect(reverse('postapp:home'))
            # return HttpResponse('<h1> POST IS CREATED </h1>')

    dict = {'form': form}
    return render(request, 'postapp/create_post.html', dict)


@login_required
def edit_post(request):
    current_user = Post.objects.filter(creator=request.user).first()
    form = Edit_Post_Form(instance=current_user)
    if request.method == 'POST':
        form = Edit_Post_Form(request.POST, request.FILES,instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'POST UPDATED')
            return HttpResponseRedirect(reverse('loginapp:user_profile'))
            # return HttpResponse('POST EDITED')
    dict = {'form': form}
    return render(request, 'postapp/edit_post.html', dict)


@login_required
def delete_post(request, pk):
    post = Post.objects.filter(pk=pk)
    post.delete()
    messages.warning(request, 'POST DELETED')
    return HttpResponseRedirect(reverse('postapp:home'))


# def myposts(request):
#     return render(request,'postapp/myposts.html')

def home(request):
    model = Post.objects.all()
    dict = {'model': model}
    return render(request, 'postapp/home.html', dict)


@login_required
def post_details(request,pk):
    post = Post.objects.get(pk=pk)
    comment_form = Add_Comment()
    if request.method == 'POST':
        comment_form = Add_Comment(request.POST)
        if comment_form.is_valid():
            commentboi = comment_form.save(commit=False)
            commentboi.user = request.user
            commentboi.post = post
            commentboi.save()
            messages.success(request,"COMMENT ADDED")
            return HttpResponseRedirect(reverse('postapp:post_details',kwargs={'pk':pk}))
    dict = {'post':post,'comment_form':comment_form}
    return render(request,'postapp/post_details.html',dict)


@login_required
def follow_view(request,username):
    follower_user = Follow.objects.get(follower=request.user)
    following_user = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower_user=follower_user,following_user=following_user)
    if not already_followed:
        followed_user = Follow(follower_user=follower_user,following_user=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('loginapp:user_profile',kwargs={'username':username}))


@login_required
def unfollow_view(request, username):
    follower_user = Follow.objects.get(follower=request.user)
    following_user = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower_user=follower_user, following_user=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('loginapp:user_profile', kwargs={'username': username}))
