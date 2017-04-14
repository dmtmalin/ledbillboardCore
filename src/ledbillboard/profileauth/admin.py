from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from ledbillboard.profileauth.models import User


class ProfileAuthAdmin(UserAdmin):
    pass

admin.site.register(User, ProfileAuthAdmin)
