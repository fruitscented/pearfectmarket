from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubtagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class SubmissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title": ("title",)}


class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name": ("name",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Subtag, SubtagAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Question, QuestionAdmin)
