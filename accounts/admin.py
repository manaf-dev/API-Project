from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser

    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.fieldsets
