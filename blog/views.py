from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog import models

def hello_world(request):
    return HttpResponse("hello world")

def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})

def blog_detail(request, id):
    blog_id = get_object_or_404(models.Post, id=id)
    return render(request, 'post_detail.html', {'blog_id': blog_id})
