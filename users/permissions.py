from rest_framework import permissions


class IsOwnerOrIsDoctor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            return obj.user == request.user or (request.user.is_authenticated and request.user.is_doctor)
        except AttributeError:
            return obj.pk == request.user.pk or (request.user.is_authenticated and request.user.is_doctor)


class IsOwnerOrIsStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            return obj.user == request.user or (request.user.is_authenticated and request.user.is_staff)
        except AttributeError:
            return obj.pk == request.user.pk or (request.user.is_authenticated and request.user.is_staff)
