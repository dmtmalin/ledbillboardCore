from django.contrib import admin

# Register your models here.
from ledbillboard.playlist.forms import ScheduleForm
from ledbillboard.playlist.models import Playlist, Schedule, MediaItem


class PlaylistAdmin(admin.ModelAdmin):
    pass


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('playlist', 'timing', )
    form = ScheduleForm


class MediaItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(MediaItem, MediaItemAdmin)
