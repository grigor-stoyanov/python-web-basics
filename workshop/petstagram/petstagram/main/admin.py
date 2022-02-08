from django.contrib import admin

# Register your models here.
from petstagram.main.models import Profile, Pet, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'description')
    inlines = (PetInlineAdmin,)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user_profile_id')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
