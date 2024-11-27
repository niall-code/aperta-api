from django.db import IntegrityError
from rest_framework import serializers

from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follow model

    The create method checks that the owner and followed_creator
    pairing does not already exist
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed_creator.username')

    class Meta:
        model = Follow
        fields = [
            'id', 'owner', 'made_at', 'followed_creator', 'followed_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
