from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Approval(models.Model):
    """
    Approval model
    """
    green_listed_post = models.ForeignKey(
        Post, related_name='green_listed', on_delete=models.CASCADE
    )
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']

    def __str__(self):
        return f"'{self.green_listed_post.title}' has been reviewed"
