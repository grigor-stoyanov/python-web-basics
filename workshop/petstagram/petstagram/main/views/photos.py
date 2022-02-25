from django.shortcuts import render, redirect

from petstagram.main.forms.photo_forms import CreatePhotoForm
from petstagram.main.models import PetPhoto


def like_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .get(pk=pk)
    ctx = {
        'pet_photo': pet_photo
    }
    return render(request, 'photo_details.html', ctx)


def photo_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    ctx = {
        'pet': instance,
        'form': form
    }
    return render(request, template_name, ctx)


def create_pet_photo(request):
    return photo_action(request, CreatePhotoForm, 'dashboard', None, 'photo_create.html')


def edit_pet_photo(request):
    return render(request, 'photo_edit.html')
