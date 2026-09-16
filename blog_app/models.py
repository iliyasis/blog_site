from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Count, Q


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_app:category_detail', kwargs={'pk': self.pk})

    def post_count(self):
        return self.posts.count()




class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ManyToManyField(Category, related_name="posts")
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)


    def get_absolute_url(self):
        return reverse('blog_app:post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return f"{ self.title }   ------------  {self.content[:25]} "

    def get_similar_post(self):
        current_categories = self.category.all()

        similar_posts = (
            Post.objects
            .exclude(pk=self.pk)
            .filter(category__in=current_categories)
            .annotate(
                similarity=Count(
                    'category',
                    filter=Q(category__in=current_categories),
                    distinct=True
                )
            )
            .order_by('-similarity', '-date_posted')
        )

        return similar_posts.first()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return f"{ self.author.username }  ------------  {self.content[:25]} "