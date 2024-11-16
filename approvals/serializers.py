from rest_framework import serializers

from approvals.models import Approval


class ApprovalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Approval model
    """
    class Meta:
        model = Approval
        fields = ['id', 'green_listed_post', 'made_at']
