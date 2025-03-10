from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (  # Keep existing fields & add custom ones
        ('Additional Info', {'fields': ('phone_number',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
