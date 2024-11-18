from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Checks the permissions of the current user.
    Ensures a user can only edit an object that they own.
    '''
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE' and request.user.is_staff:
            return True

        if request.method == 'PUT':
            data = request.data
            allowed_fields = {'reported', 'green_listed'}
            if set(data.keys()).issubset(allowed_fields):
                return True

        return obj.owner == request.user
