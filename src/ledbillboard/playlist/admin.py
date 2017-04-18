# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from ledbillboard.playlist.forms import PlaylistForm
from ledbillboard.playlist.models import Playlist, Media
from django.utils.translation import ugettext_lazy as _


class MediaInLine(admin.StackedInline):
    model = Media
    extra = 0
    inline_classes = ('grp-collapse grp-open', )
    fields = ('file', 'is_approve', )


class PlaylistInLine(admin.StackedInline):
    model = Playlist
    extra = 0
    inline_classes = ('grp-collapse grp-open', )
    fields = ('media', 'timing', )
    filter_horizontal = ('media', )


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'media', 'timing', )
    filter_horizontal = ('media', )
    form = PlaylistForm


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'duration', 'create_at', 'user', )
    search_fields = ['user__first_name', 'user__last_name']

    def filename(self, obj):
        return obj.file.name
    filename.short_description = _('File name')

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Media, MediaAdmin)
