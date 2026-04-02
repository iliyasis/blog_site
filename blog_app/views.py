from django.shortcuts import render, get_object_or_404
from blog_app.models import Post ,Category
from django.core.paginator import Paginator

# Create your views here.


page_names = {
    "home_page": "خانه",
    "post_list": "بلاگ ها",
    "category_detail": "دسته بندی ها"
}

def post_list(request):
    paginator = Paginator(Post.objects.all(), 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    page_name = page_names[request.resolver_match.url_name]
    return render(request,"blog_app/post_list.html", {"posts":posts, "page_name":page_name})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    paginator = Paginator(category.posts.all(), 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    page_name = page_names[request.resolver_match.url_name]
    return render(request, "blog_app/post_list.html", {"posts":posts, "page_name":page_name, "page_name2":category.title})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_app/post_detail.html", {"post":post})