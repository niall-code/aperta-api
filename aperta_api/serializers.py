from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    '''
    Serializes instances of the default User model.

    Adds profile_id, profile_picture, and is_staff to fields
    returned when requesting logged-in user details.
    '''
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='profile.profile_picture.url'
    )
    is_staff = serializers.ReadOnlyField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_picture', 'is_staff'
        )
