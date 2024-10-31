from rest_framework import serializers
from .models import Profile
from follows.models import Follow


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializes instances of the Profile model.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    follow_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        Returns True if the user making the request
        is the owner of the object.
        '''
        request = self.context['request']
        return request.user == obj.owner

    def get_follow_id(self, obj):
        # Will let me see if I've followed a profile
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
            'is_owner', 'follow_id'
        ]
