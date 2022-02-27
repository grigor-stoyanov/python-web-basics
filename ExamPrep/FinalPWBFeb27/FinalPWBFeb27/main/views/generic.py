from django.shortcuts import render

from FinalPWBFeb27.main.forms.profile import ProfileForm
from FinalPWBFeb27.main.helpers import get_profile, form_view
from FinalPWBFeb27.main.models import Album


def home_view(request):
    profile = get_profile()
    ctx = {
        'user': profile,
        'albums': Album.objects.all()
    }
    if profile:
        return render(request, 'home/home-with-profile.html', ctx)
    return form_view(request, ProfileForm, 'home', None, 'home/home-no-profile.html')
