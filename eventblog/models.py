from datetime import datetime

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


class Subtag(models.Model):
    tag = models.ForeignKey(Tag,
                            related_name='tag',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subtag'
        verbose_name_plural = 'subtags'

    def __str__(self):
        return self.name


class Submission(models.Model):
    your_name = models.CharField(max_length=200, default='')
    contact_information = models.CharField(max_length=200, default='')
    check_if_you_are_the_event_host = models.BooleanField(default=False)
    event_host_contact_information = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    event_date_and_time = models.CharField(max_length=200, default='')
    event_setup_time = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    vendor_fee = models.CharField(max_length=200, default='')
    additional_information = models.TextField(max_length=1000)
    event_flyer = models.ImageField(upload_to="images/", default='', null=True, blank=True)

    # Define relations
    pear_tags = models.ManyToManyField(Subtag)
    additional_pear_tags = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default='')
    content = RichTextField()
    featured_image = models.ImageField(upload_to="images/", default='')
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    # Define relations
    subtag = models.ManyToManyField(Subtag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    name = models.CharField(max_length=400, default='')
    phone_or_email = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

