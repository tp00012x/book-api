from rest_framework.permissions import BasePermission


class APIPermission(BasePermission):
    """
    Stub for permission class for API Endpoints
    """

    # Specify https method names because we don't want to allow the user to
    # update a wish list object.
    allowed_methods = ('GET', 'POST', 'DELETE', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        allow_request = True  # Stub for more permissions based logic
        return request.method in self.allowed_methods and allow_request
