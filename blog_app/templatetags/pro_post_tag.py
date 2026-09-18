from django import template
from blog_app.models import Post


register = template.Library()


@register.inclusion_tag("components/pro_post.html")
def pro_post():
    posts = Post.objects.filter(pro=True)[:6]
    return {"posts": posts}