from rest_framework import serializers
from reports.models import Report
# from posts.models import Post


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = [
            'id', 'owner', 'made_at',
            'post_id', 'post_title', 'post_text', 'post_image',
            'reason', 'explanation'
        ]
