# -*- coding: utf-8 -*-
from django.contrib import admin
from ledbillboard.playlist.models import Playlist


class PlaylistInLine(admin.StackedInline):
    model = Playlist
    extra = 0
    inline_classes = ('grp-collapse grp-open', )
    fields = ('media', 'schedule', )
    filter_horizontal = ('media', )


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
    filter_horizontal = ('media', )


admin.site.register(Playlist, PlaylistAdmin)
