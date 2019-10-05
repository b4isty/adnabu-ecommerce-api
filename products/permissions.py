from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerUser(BasePermission):
    """
    Permission class for owner of the product to modify it
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSuperUseOrReadOnly(BasePermission):
    """
    Permission class for super user to crate update delete products
    """
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return bool(request.method in SAFE_METHODS and
                        request.user.is_authernticated
                        or request.user and request.user.is_staff
                        )
        return True



