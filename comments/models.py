from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class Comment(models.Model):
    '''
    Comment model, related to User and Post
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    reported = models.BooleanField(default=False)
    green_listed = models.BooleanField(default=False)
    made_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-made_at']

    def __str__(self):
        return self.comment_text
