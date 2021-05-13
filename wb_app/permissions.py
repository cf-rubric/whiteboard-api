import rest_framework
from rest_framework import permissions
# from django.contrib.auth import get_user_model

class isAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)