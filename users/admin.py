from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailVerifications)
class EmailVerification(admin.ModelAdmin):
    pass
