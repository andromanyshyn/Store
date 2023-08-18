from rest_framework.permissions import BasePermission


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_staff or request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return request.user.is_staff or request.user.is_superuser
