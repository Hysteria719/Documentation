from rest_framework.permissions import BasePermission

class IsEmployeAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'employe')