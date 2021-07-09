from django.contrib import admin

# Register your models here.
from .models import NewUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')

    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
            
            ('General', {'fields': ('email', 'user_name', 'first_name',)}),
            ('Permissions', {'fields': ('is_staff', 'is_active',)}),
            ('Personal', {'fields': ('about',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(NewUser, UserAdminConfig)
