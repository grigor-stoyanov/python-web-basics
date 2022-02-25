from django.shortcuts import render, redirect

from petstagram.main.forms.pet_forms import CreatePetForm, DeletePetForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import Pet


def pet_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
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


def create_pet(request):
    return pet_action(request, CreatePetForm, 'profile', Pet(user_profile=get_profile()), 'pet_create.html')


def edit_pet(request, pk):
    return pet_action(request, CreatePetForm, 'profile', Pet.objects.get(pk=pk), 'pet_edit.html')


def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'pet_delete.html')