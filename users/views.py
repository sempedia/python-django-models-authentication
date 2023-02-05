from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import get_object_or_404

# Create your views here.


def index(): 
    posts = BlogPost.objects.all()
    return get_object_or_404(BlogPost, pk=id)