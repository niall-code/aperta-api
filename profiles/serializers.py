from rest_framework import serializers

from .models import Profile
from follows.models import Follow


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializes instances of the Profile model.

    Adds posts_count, followers_count, and follows_count to fields
    returned when requesting profile details. Definitions provided
    by annotate method in querysets of ProfileList and ProfileDetail
    views.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follow_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    follows_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        '''
        Returns a Boolean value for is_owner.
        If user making request is profile owner, returns True.
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_follow_id(self, obj):
        '''
        Returns a value for follow_id.
        If authenticated user has followed the profile owner,
        returns id of Follow instance. Else, returns None.

        Helps one user see whether previously followed another.
        Supports unfollowing by including follow_id in API response.
        '''
        user = self.context['request'].user
        if user.is_authenticated:
            follow = Follow.objects.filter(
                owner=user, followed_creator=obj.owner
            ).first()
            return follow.id if follow else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'profile_picture', 'made_at', 'changed_at',
            'is_owner', 'follow_id', 'posts_count', 'followers_count',
            'follows_count'
        ]
