import datetime

from django.core.validators import MinLengthValidator, URLValidator
from django.db import models

from petstagram.main.validators import only_letters_validator, file_max_size, MinDateValidator, MaxDateValidator


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    GENDER_MALE = ('Male', 'Male')
    GENDER_FEMALE = ('Female', 'Female')
    GENDER_DO_NOT_SHOW = ('Do not show', 'Do not show')
    GENDERS = [GENDER_FEMALE, GENDER_MALE, GENDER_DO_NOT_SHOW]
    # id/pk by default
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )
    profile_picture = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=GENDER_DO_NOT_SHOW,
    )


class Pet(models.Model):
    # Constants
    NAME_MAX_LENGTH = 30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    MIN_DATE = datetime.date(1920, 1, 1)
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    # fields
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    type = models.CharField(
        choices=TYPES,
        max_length=max(len(x) for (x, _) in TYPES)
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator(MIN_DATE),
        )
    )
    # relations one-to-one,one-to-many,many-to-many
    # one to many one user can have many pets but every pet 1 user
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.birth_date.year

    class Meta:
        # makes a unique pairing u can have multiple same pet names
        # with different owners but 1 owner has unique pets
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            file_max_size,
        )
    )
    # TODO validate at least 1 pet
    tagged_pets = models.ManyToManyField(
        Pet,
        null=False,
    )
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
