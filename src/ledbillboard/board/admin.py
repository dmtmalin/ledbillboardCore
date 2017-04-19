# -*- coding: utf-8 -*-
from django.contrib import admin

from ledbillboard.board.models import Board
from ledbillboard.playlist.admin import PlaylistInLine


class BoardInLine(admin.StackedInline):
    model = Board
    extra = 0
    inline_classes = ('grp-collapse grp-open', )
    fields = ('name', 'slug', 'lat', 'lon', )
    prepopulated_fields = {'slug': ('name', )}


class BoardAdmin(admin.ModelAdmin):
    model = Board
    inlines = (PlaylistInLine, )
    list_display = ('id', 'name', 'company', 'lat', 'lon', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Board, BoardAdmin)
