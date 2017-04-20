from django.contrib import admin
from ledbillboard.mediacontent.models import Media


class MediaInLine(admin.StackedInline):
    model = Media
    extra = 0
    inline_classes = ('grp-collapse grp-open', )
    fields = ('file', 'is_approve', )


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'duration', 'create_at', 'user', )
    search_fields = ['user__first_name', 'user__last_name']


admin.site.register(Media, MediaAdmin)
