from django.db import IntegrityError
from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model

    The create method handles unique constraint
    on 'owner' and 'liked_post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'made_at', 'owner', 'liked_post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
