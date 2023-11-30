from functools import reduce
from operator import or_

from blog.utils import slugify
from django.db.models import Q
from django.shortcuts import render

from .forms import PostForm
from .models import *
from .qforms import QForm


def home(request):
    posts = Post.objects.all().filter(is_published=True).order_by('-created_at')
    subtags = Subtag.objects.all()
    tags = Tag.objects.all()

    return render(request, 'home.html', {
        'posts': posts,
        'subtags': subtags,
        'tags': tags,
    })


def subtag(request, slug):
    posts = Post.objects.filter(subtag__slug=slug).filter(is_published=True)
    requested_subtag = Subtag.objects.get(slug=slug)
    subtags = Subtag.objects.all()
    tags = Tag.objects.all()

    return render(request, 'tag.html', {
        'posts': posts,
        'subtag': requested_subtag,
        'subtags': subtags,
        'tags': tags,
    })


def post(request, slug):
    requested_post = Post.objects.get(slug=slug)
    subtags = Subtag.objects.all()
    tags = Tag.objects.all()

    # Related Posts
    ## Get all the tags related to this article
    post_tags = requested_post.tag.all()
    ## Filter all posts that contain tags which are related to the current post, and exclude the current post
    related_posts_ids = (
        Post.objects.all()
        .filter(tag__in=post_tags)
        .exclude(id=requested_post.id)
        .values_list("id")
    )

    related_posts = Post.objects.filter(pk__in=related_posts_ids)

    return render(
        request,
        "post.html",
        {
            "post": requested_post,
            "subtags": subtags,
            'tags': tags,
            "related_posts": related_posts,
        },
    )


def search(request):
    posts = Post.objects.all()
    subtags = Subtag.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'subtags': subtags,
        'tags': tags,
        'keyword': ''
    }
    keyword = request.POST.get('keyword')
    if keyword:
        keyword = keyword.lower()
        posts = Post.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(subtag__name__icontains=keyword)).distinct()
        context = {
            'posts': posts,
            'subtags': subtags,
            'tags': tags,
            'keyword': keyword
        }

    return render(request, 'search.html', context)


def tagfilter(request):
    posts = Post.objects.all()
    subtags = Subtag.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.all()
    for word in request.POST.getlist('q'):
        posts = posts.filter(Q(subtag__name__icontains=word))
    context = {
        'posts': posts,
        'subtags': subtags,
        'tags': tags,
    }

    return render(request, 'tagfilter.html', context)


def submissions(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, "submissions.html", {"form": form})


def about(request):
    qform = QForm()
    if request.method == 'POST':
        qform = QForm(request.POST, request.FILES)
        if qform.is_valid():
            qform.save()
    return render(request, "about.html", {"qform": qform})
