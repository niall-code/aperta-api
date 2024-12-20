from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    """
    Follow model, related to 'owner' and 'followed_creator'.
    """
    owner = models.ForeignKey(
        User, related_name='follows', on_delete=models.CASCADE
    )
    followed_creator = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE
    )
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['owner', 'followed_creator']

    def __str__(self):
        return f'{self.owner} follows {self.followed_creator}'
