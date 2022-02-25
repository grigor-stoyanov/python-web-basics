from django import forms

from petstagram.main.helpers import BootStrapFormMixin
from petstagram.main.models import Profile, PetPhoto


class EditProfileForm(BootStrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.GENDER_DO_NOT_SHOW
        self.fields['birth_date'].input_type = 'date'

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                    'placeholder': 'Enter Date of Birth',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
            'gender': forms.Select(
                choices=Profile.GENDERS,
            )
        }


# class CreateProfileForm(BootStrapFormMixin, forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#         self.initial['gender'] = Profile.GENDER_DO_NOT_SHOW
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'profile_picture')
#         # the hard way to style form
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Enter First Name',
#                 }
#             ),
#             'last_name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Enter Last Name',
#                 }
#             ),
#             'profile_picture':forms.TextInput(
#                 attrs={
#                     'placeholder':'Enter Email'
#                 }
#             )
#         }


class DeleteProfileForm(forms.ModelForm):
    # we will overwrite save method
    def save(self, commit=True):
        # self.instance = profile
        pets = self.instance.pet_set.all()
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'email', 'profile_picture', 'description', 'birth_date', 'gender')
