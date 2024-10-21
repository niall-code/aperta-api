from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    '''
    Adds profile_id and profile_picture to fields returned when
    requesting logged-in user details.
    '''
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='profile.profile_picture.url'
    )

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_picture'
        )
