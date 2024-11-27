from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='owner.profile.profile_picture.url'
    )
    made_at = serializers.SerializerMethodField()
    changed_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Checks whether user owns the comment
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_made_at(self, obj):
        '''
        Converts made_at value to human readable
        '''
        return naturaltime(obj.made_at)

    def get_changed_at(self, obj):
        '''
        Converts changed_at value to human readable
        '''
        return naturaltime(obj.changed_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_picture',
            'commented_on_post', 'made_at', 'changed_at', 'comment_text',
            'reported', 'green_listed',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    The post is read only field so do not have to set it on each update
    """
    commented_on_post = serializers.ReadOnlyField(source='commented_on_post.id')
