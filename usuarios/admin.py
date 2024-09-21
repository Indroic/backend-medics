from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import action
from .models import Usuario
from django.urls import reverse
from django.shortcuts import redirect
from unfold import forms
from django.contrib.auth.admin import UserAdmin


class UsuarioAdmin(UserAdmin, ModelAdmin):
    add_form = forms.UserCreationForm
    
    list_display = (
        "username",
        "email",
        "create_at",
        "update_at",
        "is_active",
        "is_staff",
        "is_superuser"
    )
    list_filter = ("create_at", "update_at")

    search_fields = ("username", "email", "ci", "id")

    fieldsets = (
        (
            "Informacion de Cuenta",
            {"fields": ("username", "avatar", "password")},
        ),
        (
            "Informacion Personal",
            {"fields": ("first_name", "last_name", "ci", "email")},
        ),
        (
            "Seguridad",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("tab",),
            },
        ),
    )

    actions_row = ["delete_user"]

    @action(
        description="Eliminar Usuario",
        url_path="delete-user"
    )
    def delete_user(self, request, object_id):
        
        return redirect(reverse("admin:usuarios_usuario_delete", args=[object_id]))


admin.site.register(Usuario, UsuarioAdmin)
