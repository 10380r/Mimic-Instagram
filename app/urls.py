from django.urls import path
from . import views

urlpatterns = [
        path('',       views.index,  name='index'),
        path('post',   views.post,   name='post'),
        path('recommend',   views.recommend,   name='recommend'),
        path('like/<int:like_id>',   views.like, name='like'),
        ]
