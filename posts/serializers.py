from rest_framework import serializers

from posts.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    '''
    Serializes instances of the Post model.

    Returns additional fields when requesting post details.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='owner.profile.profile_picture.url'
    )
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        '''
        Enforces that a user-uploaded image has a file size of 2MB
        or less and that its width and height do not exceed 4096px.
        '''
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
        '''
        Returns a Boolean value for is_owner.
        If user making request is post owner, returns True.
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        '''
        Returns a value for like_id.
        If authenticated user has liked the post,
        returns id of Like instance. Else, returns None.

        Helps a user see whether previously liked a post.
        Supports unliking by including like_id in API response.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, liked_post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_picture', 'made_at', 'changed_at',
            'title', 'post_text', 'image', 'reported',
            'green_listed', 'like_id', 'likes_count',
            'comments_count'
        ]
