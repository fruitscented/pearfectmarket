from django.shortcuts import render

from .models import *


def home(request):
    posts = Post.objects.all().filter(is_published=True)
    tags = Tag.objects.all()

    return render(request, 'home.html', {
        'posts': posts,
        'tags': tags,
    })

def tag(request, slug):
    posts = Post.objects.filter(tag__slug=slug).filter(is_published=True)
    requested_tag = Tag.objects.get(slug=slug)
    tags = Tag.objects.all()

    return render(request, 'tag.html', {
        'posts': posts,
        'tag': requested_tag,
        'tags': tags,
    })


def post(request, slug):
    requested_post = Post.objects.get(slug=slug)
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
            "tags": tags,
            "related_posts": related_posts,
        },
    )

