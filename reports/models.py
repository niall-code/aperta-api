from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Report(models.Model):
    """
    Report model
    """
    reported_post = models.ForeignKey(
        Post, related_name='reported', on_delete=models.CASCADE
    )
    reason = models.IntegerField(
        choices=[
            (1, "Graphic violence"),
            (2, "Explicit sexual content"),
            (3, "Sexualization of minors"),
            (3, "Inciting hatred"),
            (4, "Encouraging suicide or self-harm"),
            (5, "Attempting to defraud"),
            (6, "Advertising illegal products"),
            (7, "Blatant copyright infringement"),
            (8, "Other serious reason (please describe in 'explanation')")
        ],
        blank=False
    )
    explanation = models.TextField(blank=True)
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Chronological order, to address oldest most urgently
        ordering = ['made_at']

    def __str__(self):
        return f"'{self.reported_post.title}' was reported"
