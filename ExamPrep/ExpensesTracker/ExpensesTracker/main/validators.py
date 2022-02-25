from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters")


def below_zero_validator(value):
    if value < 0:
        raise ValidationError("Value must be positive")


def image_size_validator(value):
    file_size = value.file.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f"Max size of file is {limit_mb} MB")
