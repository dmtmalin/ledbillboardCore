from django.contrib import admin

from ledbillboard.board.admin import BoardInLine
from ledbillboard.company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    inlines = (BoardInLine, )
    list_display = ('id', 'name', )

admin.site.register(Company, CompanyAdmin)
