from rest_framework.permissions import BasePermission
from datetime import timedelta, date


class IsValid(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.date >= date.today()+timedelta(days=3):
            return True
        else:
            return False


class IsOwner(BasePermission):
    message = "You're not the owner of the Booking"
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_staff:
            return True
        else:
            return False
