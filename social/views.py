from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import RegisterForm, PostForm, CommentForm, ProfileForm
from .models import Post, Like, Follow

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else: form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def feed(request):
    posts = Post.objects.select_related("author").prefetch_related("likes", "comments__author")
    liked_ids = set(Like.objects.filter(user=request.user).values_list("post_id", flat=True))
    return render(request, "social/feed.html", {"posts": posts, "liked_ids": liked_ids, "post_form": PostForm(), "comment_form": CommentForm()})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False); post.author = request.user; post.save()
            messages.success(request, "Your post has been published.")
        else: messages.error(request, "Please check your post and try again.")
    return redirect("feed")

@login_required
@require_POST
def toggle_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created: like.delete()
    return redirect(request.POST.get("next") or "feed")

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False); comment.post = post; comment.author = request.user; comment.save()
    return redirect(request.POST.get("next") or "feed")

@login_required
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    post.delete()
    return redirect("feed")

@login_required
def profile(request, username):
    person = get_object_or_404(User, username=username)
    profile_obj = person.profile
    if request.method == "POST" and request.user == person:
        form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if form.is_valid(): form.save(); messages.success(request, "Profile updated.")
        return redirect("profile", username=username)
    form = ProfileForm(instance=profile_obj) if request.user == person else None
    posts = person.posts.select_related("author").prefetch_related("likes", "comments__author")
    is_following = request.user.is_authenticated and Follow.objects.filter(follower=request.user, following=person).exists()
    context = {"person": person, "profile_obj": profile_obj, "posts": posts, "is_following": is_following,
               "followers_count": person.followers.count(), "following_count": person.following.count(),
               "form": form, "liked_ids": set(Like.objects.filter(user=request.user).values_list("post_id", flat=True)) if request.user.is_authenticated else set(),
               "comment_form": CommentForm()}
    return render(request, "social/profile.html", context)

@login_required
@require_POST
def toggle_follow(request, username):
    person = get_object_or_404(User, username=username)
    if person != request.user:
        relation, created = Follow.objects.get_or_create(follower=request.user, following=person)
        if not created: relation.delete()
    return redirect("profile", username=username)
