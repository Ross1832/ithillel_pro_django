from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def valid_email_domains(value):
    valid_domain = ['@gmail.com', '@yahoo.com', ]
    for domain in valid_domain:
        if domain in value:
            break
    else:
        raise ValidationError('Invalid email address.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if str(args[0]).endswith(domain):
                break
            else:
                raise ValidationError(f"Invalid email address. The domain <{str(args[0]).split('@')[1]}> not valid.")
