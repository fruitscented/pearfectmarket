from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>', views.post, name='post'),
    path('tag/<slug:slug>', views.tag, name='tag'),
]