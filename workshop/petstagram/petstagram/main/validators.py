# validators must raise validation error or return none
from django.core.exceptions import ValidationError


def always_valid(chars):
    def validator(value):
        pass

    return validator


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError


def file_max_size(value):
    file_size = value.file.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)
