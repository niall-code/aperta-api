from rest_framework import serializers
from .models import Approval


class ApprovalSerializer(serializers.ModelSerializer):
    """
    Serializer for the Approval model
    """
    class Meta:
        model = Approval
        fields = ['id', 'owner', 'approved_post', 'made_at']
