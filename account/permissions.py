from rest_framework import permissions

from account.models import PrimaryAccess


class PrimaryAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if self.exist_token(request):
            return True
        return False

    def exist_token(self, request):
        token = request.META.get('HTTP_X_ACCESS_TOKEN')
        if token:
            return PrimaryAccess.objects.filter(token=token, is_active=True).exists()
        return False