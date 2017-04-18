# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from ledbillboard.account.models import User
from ledbillboard.board.admin import BoardInLine
from ledbillboard.playlist.admin import MediaInLine
from django.utils.translation import ugettext_lazy as _


class AccountAdmin(UserAdmin):
    inlines = (MediaInLine, BoardInLine, )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal information'), {
            'fields': ('first_name', 'last_name', 'phone', 'birthday', )
        }),
        (_('Permissions'), {'fields': ('is_active',  'is_lessor', )}),
        (_('Administration'), {'fields': ('is_staff', 'is_superuser', )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    list_display = ('first_name', 'last_name', 'email', 'last_login', 'date_joined', 'is_active', 'is_staff', )
    readonly_fields = ('last_login', 'date_joined',)
    ordering = ('first_name', 'last_name', )


admin.site.register(User, AccountAdmin)
