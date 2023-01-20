from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from core.models import Usuario, Status, Chats, bot, Empreendimentos

admin.site.register(Chats)
admin.site.register(Status)
admin.site.register(Usuario)
admin.site.register(bot)
admin.site.register(Empreendimentos)

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password",'password_confirmation')}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "foto", "telefone", "recados")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )