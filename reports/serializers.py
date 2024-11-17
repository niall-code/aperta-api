from rest_framework import serializers
from reports.models import Report
from posts.models import Post


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = [
            'id', 'owner', 'reported_post',
            'reason', 'explanation', 'made_at'
        ]
