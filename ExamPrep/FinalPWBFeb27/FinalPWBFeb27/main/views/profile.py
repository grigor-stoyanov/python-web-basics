from django.shortcuts import render

from FinalPWBFeb27.main.forms.profile import DeleteProfileForm
from FinalPWBFeb27.main.helpers import get_profile, form_view
from FinalPWBFeb27.main.models import Album


def profile_details_view(request):
    ctx = {
        'profile': get_profile(),
        'albums': Album.objects.all().count()
    }
    return render(request, 'profile/profile-details.html', ctx)


def profile_delete_view(request):
    return form_view(request, DeleteProfileForm, 'home', get_profile(), 'profile/profile-delete.html')
