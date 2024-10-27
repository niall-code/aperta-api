from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='created_by.profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='created_by.profile.profile_picture.url'
    )

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
