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
        pass


class Post(models.Model):
    """A Post"""
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(
        auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.content)[:20]

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author.username,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes
        }

    class Meta:
        ordering = ("-timestamp",)
