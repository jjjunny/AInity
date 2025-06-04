from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('student_id', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('student_id', 'name')
    ordering = ('student_id',)

    fieldsets = (
        (None, {'fields': ('student_id', 'password')}),
        ('개인 정보', {'fields': ('name',)}),
        ('권한', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('중요한 날짜', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    from django.contrib import admin
    from .models import Notice

    admin.site.register(Notice)
