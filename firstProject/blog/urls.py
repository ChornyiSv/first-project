from django.contrib import admin
from django.urls import path, include
from blog.views import post_list, post_update, post_create, post_delete, post_detail

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),   # http://127.0.0.1:8000/blog/
    path('update/<int:id>/', post_update, name='post_update'),
    path('create/', post_create, name='post_create'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
    path('delete/<int:id>/', post_delete, name='post_delete')


]