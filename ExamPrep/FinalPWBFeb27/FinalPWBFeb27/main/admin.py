from django.contrib import admin

from FinalPWBFeb27.main.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name',)
