from django.contrib import admin

from ledbillboard.references.models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', )

admin.site.register(Schedule, ScheduleAdmin)
