from rest_framework import permissions

class IsCarLegitorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.make == request.user

class CarBlocklistPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        ip = request.META['REMOTE_ADDR']
        block = Blocklist.objects.filter(ip_addr=ip).exists()
        return not block