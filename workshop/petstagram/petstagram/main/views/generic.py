from django.shortcuts import render, redirect

from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


def show_home(request):
    ctx = {
        'hide_additional_nav_items': True,
    }
    return render(request, 'home_page.html', ctx)


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('401')
    pet_photos = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .filter(tagged_pets__user_profile=profile) \
        .distinct()

    ctx = {
        'pets': pet_photos,
    }
    return render(request, 'dashboard.html', ctx)