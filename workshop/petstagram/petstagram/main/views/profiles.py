from django.shortcuts import render, redirect

from petstagram.main.forms.profile_forms import EditProfileForm, DeleteProfileForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto, Pet, Profile


def show_profile(request):
    profile = get_profile()
    profile_pets = Pet.objects \
        .filter(user_profile=profile)
    # pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=profile_pets).distinct()
    total_likes_count = sum(pp.likes for pp in pet_photos)
    # gives us unique pictures
    total_images_count = len(pet_photos)
    ctx = {
        'profile': profile,
        'my_pets': profile_pets,
        'total_likes_count': total_likes_count,
        'total_images_count': total_images_count
    }
    return render(request, 'profile_details.html', ctx)


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    ctx = {
        'form': form
    }
    return render(request, template_name, ctx)


def create_profile(request):
    if request.method == 'POST':
        # create form with post
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # create empty form
        form = EditProfileForm()
    ctx = {
        'form': form
    }
    return render(request, 'profile_create.html', ctx)
# def create_profile(request):
#     return profile_action(request, CreateProfileForm, 'index', None, 'profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile', get_profile(), 'profile_edit.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')
