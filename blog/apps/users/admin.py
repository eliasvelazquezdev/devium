from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_staff")
    readonly_fields = ('id',)
    list_filter = ("first_name", "last_name", "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name", "about", "avatar",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "first_name", "last_name", "about", "avatar")
        }),
    )
    search_fields = ("email",)
    ordering = ("date_joined",)


admin.site.register(CustomUser)