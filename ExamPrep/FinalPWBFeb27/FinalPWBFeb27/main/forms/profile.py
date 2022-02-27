from django import forms

from FinalPWBFeb27.main.models import Profile, Album


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'username'
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'email'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'age'
                }
            )

        }
