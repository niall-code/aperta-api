from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
# from comments.models import Comment


class Report(models.Model):
    """
    Report model, related to 'owner' and 'reported_post'
    """
    post_id = models.IntegerField(null=True)
    post_title = models.CharField(max_length=200, null=True)
    post_text = models.TextField(blank=True, null=True)
    post_image = models.CharField(max_length=500, blank=True, null=True)

    reason = models.IntegerField(
        choices=[
            (1, "Graphic violence"),
            (2, "Explicit sexual content"),
            (3, "Sexualization of minors"),
            (4, "Inciting hatred"),
            (5, "Encouraging suicide or self-harm"),
            (6, "Attempting to defraud"),
            (7, "Advertising illegal products"),
            (8, "Blatant copyright infringement"),
            (9, "Other serious reason (please describe in 'explanation')")
        ],
        blank=False
    )
    explanation = models.TextField(blank=True)
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['made_at']

    def __str__(self):
        return f'{self.post_title}'
