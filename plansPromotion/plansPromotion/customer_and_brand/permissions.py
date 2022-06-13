from rest_framework import permissions

class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

class IsBrandPromoterOrCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.user_type == 'BP':
                return True
            else:
                return False
        else:
            return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.username and request.user.user_type == 'BP'