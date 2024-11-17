from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Approval(models.Model):
    """
    Approval model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_post = models.ForeignKey(
        Post, related_name='approvals', on_delete=models.CASCADE
    )
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['owner', 'approved_post']

    def __str__(self):
        return f'{self.approved_post.title}'
