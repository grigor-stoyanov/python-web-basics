from django.core.validators import MinLengthValidator
from django.db import models

from FinalPWBFeb27.main.validators import MaxFileSizeValidator, username_validator, below_zero_validator


class Profile(models.Model):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 15
    MAX_FILE_SIZE = 5
    username = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            username_validator,
        )
    )
    email = models.EmailField()
    age = models.IntegerField(
        blank=True, null=True,
        validators=(
            below_zero_validator,
        )
    )


class Album(models.Model):
    NAME_MAX_LENGTH = 30
    GENRES = [
        "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music",
        "Hip Hop Music", "Other"
    ]
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    artist = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    genre = models.CharField(
        max_length=NAME_MAX_LENGTH,
        choices=(
            (genre, genre) for genre in GENRES
        )
    )
    description = models.TextField(
        blank=True, null=True
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(below_zero_validator,)
    )
