from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    Blogs= Blog.objects.all()
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})
