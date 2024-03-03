from rest_framework.permissions import BasePermission


class RolesMixin:
    ROLES = (
        ('Учитель', 'Учитель'),
        ('Студент', 'Студент')
    )


class IsTeacher(BasePermission, RolesMixin):
    def has_permission(self, request, view):
        return request.user.role == self.ROLES[0][1] \
            if request.user.is_authenticated else False


class IsStudent(BasePermission, RolesMixin):
    def has_permission(self, request, view):
        return request.user.role == self.ROLES[1][1] \
            if request.user.is_authenticated else False
