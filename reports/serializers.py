from rest_framework import serializers
from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    '''
    Serializes the Report model
    '''
    class Meta:
        model = Report
        fields = [
            'id', 'made_at',
            'post_id', 'post_title', 'post_text', 'post_image',
            'reason', 'explanation'
        ]
