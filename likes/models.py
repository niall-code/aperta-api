from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['owner', 'liked_post']

    def __str__(self):
        return f'{self.owner} {self.liked_post}'
