from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings



class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='')

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='')
    content = RichTextField()
    featured_image = models.ImageField(upload_to="images/", default='')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    # Define relations
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
