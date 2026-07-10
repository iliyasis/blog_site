from django.shortcuts import render

from .forms import *

# Create your views here.

def home_page(request):
    active_head = "home_page"
    return render(request, "home_app/index.html", {"active_head": active_head})

def contact_us_page(request):
    if request.method == "POST":
        form = contactus_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('full_name'))

    else:
        form = contactus_form()
    active_head = "contact_us"
    return render(request, "home_app/contact_us.html", {"active_head": active_head, "form": form})