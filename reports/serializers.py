from rest_framework import serializers
from reports.models import Report
from posts.models import Post


class ReportSerializer(serializers.ModelSerializer):
    reported_post = serializers.ReadOnlyField(source='reported_post.id')

    class Meta:
        model = Report
        fields = [
            'id', 'reported_post', 'reason', 'explanation', 'made_at'
        ]
