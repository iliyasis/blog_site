from django.shortcuts import render, get_object_or_404
from blog_app.models import Post ,Category

# Create your views here.

def post_list(request):
    active_head = "post_list"
    posts = Post.objects.all()
    return render(request,"blog_app/post_list.html", {"posts":posts, "active_head":active_head})

def category_detail(request, pk):
    print(pk)
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.all()
    return render(request, "blog_app/post_list.html", {"posts":posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_app/post_detail.html", {"post":post})