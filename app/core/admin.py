from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


# Resgister the UserAdmin class to the User model.
admin.site.register(models.User, UserAdmin)
