from django import forms

from petstagram.main.helpers import BootStrapFormMixin
from petstagram.main.models import PetPhoto, Pet
from petstagram.main.validators import file_max_size


class CreatePhotoForm(BootStrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')

        widgets = {
            'photo': forms.FileInput(
                attrs={'class': 'form-control-file'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter Description'}
            )
        }
