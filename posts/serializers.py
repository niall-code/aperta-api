from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='created_by.profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='created_by.profile.profile_picture.url'
    )

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.created_by

    class Meta:
        model = Post
        fields = [
            'id', 'created_by', 'is_owner', 'profile_id',
            'profile_picture', 'made_at', 'changed_at',
            'title', 'post_text', 'image'
        ]
