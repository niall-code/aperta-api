from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    post_id = serializers.ReadOnlyField(source='reported_post.id')
    title = serializers.ReadOnlyField(source='reported_post.title')
    post_text = serializers.ReadOnlyField(source='reported_post.post_text')
    image = serializers.SerializerMethodField()
    reason_text = serializers.ReadOnlyField(source='get_reason_display')

    def get_image(self, obj):
        if obj.reported_post.image:
            return obj.reported_post.image.url
        else:
            return '../placeholder_n7mqkw.jpg'

    class Meta:
        model = Report
        fields = [
            'id', 'owner', 'made_at',
            'post_id', 'title', 'post_text', 'image',
            'reason', 'reason_text', 'explanation'
        ]
