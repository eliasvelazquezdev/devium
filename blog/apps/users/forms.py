from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        read_only_fields = ("id",)
        fields = ("email", "first_name", "last_name", "avatar", "about", "is_active", "is_staff")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        read_only_fields = ("id",)
        fields = ("email", "first_name", "last_name", "about", "avatar", "is_active", "is_staff")