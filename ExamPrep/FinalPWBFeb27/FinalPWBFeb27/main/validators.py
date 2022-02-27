from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def username_validator(value):
    if not value.replace('_', '').isalnum():
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def below_zero_validator(value):
    if value < 0:
        raise ValidationError("Value must be positive")


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__bytes_to_megabytes(self.max_size):
            raise ValidationError(self.__get_exeption_message(self.max_size))

    def __bytes_to_megabytes(self, value):
        return value * 1024 * 1024

    def __get_exeption_message(self, value):
        return f'File is more than {value:.2f} MB!'
