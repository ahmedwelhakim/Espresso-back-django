from django.core.exceptions import ValidationError


def validate_file_size(value, file_size):
    limit = file_size * 1024 * 1000
    if value.size > limit:
        raise ValidationError(f'File too large. Size should not exceed {int(file_size)} MiB.')
