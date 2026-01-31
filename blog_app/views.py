from django.shortcuts import render
from blog_app.models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,"blog_app/post_list.html", {"posts":posts})