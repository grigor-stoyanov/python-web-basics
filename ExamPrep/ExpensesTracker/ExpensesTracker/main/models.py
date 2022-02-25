from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from ExpensesTracker.main.validators import only_letters_validator, below_zero_validator, image_size_validator


class Profile(models.Model):
    NAME_MIN_LENGTH = 2
    first_name = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(NAME_MIN_LENGTH),
                    only_letters_validator
                    )
    )
    last_name = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(NAME_MIN_LENGTH),
                    only_letters_validator
                    )
    )
    budget = models.FloatField(
        default=0,
        validators=(below_zero_validator,)
    )
    profile_image = models.ImageField(
        blank=True, null=True, default='static/images/user.png',
        upload_to='profile_pic',
        validators=(image_size_validator,)
    )


class Expense(models.Model):
    title = models.CharField(
        max_length=30
    )
    expense_image = models.URLField()
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
