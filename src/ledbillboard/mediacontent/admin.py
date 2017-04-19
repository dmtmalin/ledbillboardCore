from django.contrib import admin

from ledbillboard.mediacontent.models import Media
from django.utils.translation import ugettext_lazy as _


class MediaInLine(admin.StackedInline):
    model = Media
    extra = 0
    inline_classes = ('grp-collapse grp-open', )
    fields = ('file', 'is_approve', )


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'duration', 'create_at', 'user', )
    search_fields = ['user__first_name', 'user__last_name']

    def filename(self, obj):
        return obj.file.name
    filename.short_description = _('File name')

admin.site.register(Media, MediaAdmin)
