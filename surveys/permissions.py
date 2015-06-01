from rest_framework import permissions

# allow posting surveys for anon users
safe_plus_post = permissions.SAFE_METHODS + [u'POST']

# TODO: Allow creation of survey for un-authenticated user
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.safe_plus_post:
            return True

        # Write permissions are only allowed to the owner of the survey
        return obj.owner == request.user

