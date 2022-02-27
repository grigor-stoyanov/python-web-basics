from django import forms

from FinalPWBFeb27.main.helpers import DisabledFormMixin
from FinalPWBFeb27.main.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description'
                }
            )
            ,
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                }
            )
        }


class DeleteAlbumForm(DisabledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Album
        fields = '__all__'
