from django.contrib import admin

from main import models

@admin.register(models.Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", ) 