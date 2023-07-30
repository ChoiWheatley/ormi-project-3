from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import Member

class Admin(admin.ModelAdmin):
    list_display = ["email", "nickname", "is_staff", "is_superuser", "is_active", "born_year", "job"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Nickname", {"fields": ["nickname"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]

    add_fieldsets = [
        (None, {"classes": ["wide"],
                "fields": ["email", "nickname", "password1", "password2"]})
    ]


admin.site.register(Member, Admin)
admin.site.unregister(Group)