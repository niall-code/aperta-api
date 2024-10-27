from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Creates an instance of Post.
    """
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)
    post_text = models.TextField(blank=True)
    reported = models.BooleanField(default=False)
    green_listed = models.BooleanField(default=False)
    made_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-made_at']

    def __str__(self):
        return f'{self.id} {self.title}'
