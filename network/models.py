from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    """A Profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        User, related_name="followed_by", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    avatar_url = models.URLField(blank=True)
    bio = models.TextField(default="No bio...")

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ("-created",)

    def profile_posts(self):
        return self.user.post_set.all().order_by("-timestamp")


class Post(models.Model):
    """A Post"""
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.content)[:20]

    class Meta:
        ordering = ("-timestamp",)
