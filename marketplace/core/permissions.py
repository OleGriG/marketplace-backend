from rest_framework import permissions


class OnlySallers(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_saller


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
