from django.db import models
from django.contrib.auth.models import User


class Block(models.Model):
    """
    Block model, related to 'owner' and 'blocked_user'.
    """
    owner = models.ForeignKey(
        User, related_name='blocks', on_delete=models.CASCADE
    )
    blocked_user = models.ForeignKey(
        User, related_name='blockers', on_delete=models.CASCADE
    )
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-made_at']
        unique_together = ['owner', 'blocked_user']

    def __str__(self):
        return f'{self.owner} blocks {self.blocked_user}'
