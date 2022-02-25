from pyexpat import model

from django import forms
from django.core.exceptions import ValidationError

from ExpensesTracker.main.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        widgets = {
            'profile_image': forms.ClearableFileInput(
                attrs={'class': 'form-file'}
            )
        }


class ExpenseForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Price cannot be negative or zero!')
        return price

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class DisabledFormMixin:
    def _init_disabled(self):
        for _, field in self.fields.items():
            setattr(field, 'disabled', 'disabled')


class DeleteExpenseForm(DisabledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Expense.objects.all().delete()
        self.instance.delete()
        return self.instance
    class Meta:
        model = Profile
        fields = ()
