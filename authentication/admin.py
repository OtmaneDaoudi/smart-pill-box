from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import RoleBasedUser

# Register your models here.
class RoleBasedUserInline(admin.StackedInline):
    model = RoleBasedUser
    can_delete = False
    verbose_name_plural = "rolebasedusers"

class UserAdmin(BaseUserAdmin):
    inlines = [RoleBasedUserInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)