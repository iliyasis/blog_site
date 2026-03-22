from django.shortcuts import render

# Create your views here.

def home_page(request):
    active_head = "home_page"
    return render(request, "home_app/index.html", {"active_head": active_head})