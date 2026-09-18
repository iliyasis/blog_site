from datetime import timedelta

from django import template
from django.utils import timezone

from blog_app.models import Post


register = template.Library()


@register.inclusion_tag("components/banner_post.html")
def most_viewed_posts():

    # 30 روز قبل
    thirty_days_ago = timezone.now() - timedelta(days=30)

    # پست‌های منتشر شده در 30 روز اخیر
    recent_posts = Post.objects.filter(
        date_posted__gte=thirty_days_ago
    )

    # اگر حداقل 4 پست در 30 روز اخیر وجود داشت
    if recent_posts.count() >= 4:

        posts = recent_posts.order_by(
            "-views",
            "-date_posted"
        )[:4]

    # اگر کمتر از 4 پست وجود داشت
    else:

        posts = Post.objects.order_by(
            "-views",
            "-date_posted"
        )[:4]

    return {
        "posts": posts
    }