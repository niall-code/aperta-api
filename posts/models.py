from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a post.

    In a Post instance, 'owner' field associated with a User instance.

    For an image-focused post, the owner may leave 'post_text' blank.
    For a text-focused post, the owner may leave 'image' blank.

    'reported' defaults to False. When True, post hidden on front end.
    'green_listed' defaults to False. When True, "Report" button absent
    on front end.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
