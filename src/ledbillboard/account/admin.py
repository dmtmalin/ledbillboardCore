# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from ledbillboard.account.models import User
from ledbillboard.mediacontent.admin import MediaInLine
from django.utils.translation import ugettext_lazy as _


class AccountAdmin(UserAdmin):
    inlines = (MediaInLine, )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal information'), {
            'fields': ('username', 'phone', 'birthday', )
        }),
        (_('Company'), {'fields': ('company', )}),
        (_('Permissions'), {'fields': ('is_active',  'is_lessor', )}),
        (_('Administration'), {'fields': ('is_staff', 'is_superuser', )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )
    list_display = ('id', 'username', 'email', 'company', 'is_active', 'is_staff', 'is_lessor', )
    readonly_fields = ('last_login', 'date_joined',)
    ordering = ('username', )


admin.site.register(User, AccountAdmin)
