from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>', views.post, name='post'),
    path('subtag/<slug:slug>', views.subtag, name='subtag'),
    path('search', views.search, name='search'),
    path('tagfilter', views.tagfilter, name='tagfilter'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')
]