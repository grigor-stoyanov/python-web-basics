from django.shortcuts import render, redirect

# Create your views here.
from petstagram.main.models import Profile, PetPhoto, Pet


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    ctx = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', ctx)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = set(PetPhoto.objects
                     .prefetch_related('tagged_pets')
                     .filter(tagged_pets__user_profile=profile))
    ctx = {
        'pets': pet_photos,
    }
    return render(request, 'dashboard.html', ctx)


def show_profile(request):
    profile = get_profile()
    profile_pets = Pet.objects \
        .filter(user_profile=profile)
    ctx = {
        'profile': profile,
        'my_pets': profile_pets
    }
    return render(request, 'profile_details.html', ctx)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .get(pk=pk)
    ctx = {
        'pet_photo': pet_photo
    }
    return render(request, 'photo_details.html', ctx)


def like_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)
