from django import template
from blog_app.models import Category

register = template.Library()


@register.inclusion_tag("components/categories.html")
def show_categories():
    categories = Category.objects.all()[:5]

    return {
        "categories": categories
    }