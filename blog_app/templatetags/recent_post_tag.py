from django import template
from blog_app.models import Post

register = template.Library()


@register.inclusion_tag("components/recent_post.html")
def recent_post():
    posts = Post.objects.all().order_by("-date_updated")[:4]

    return {
        "posts": posts
    }