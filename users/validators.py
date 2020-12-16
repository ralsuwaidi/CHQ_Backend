from django.core.exceptions import ValidationError
import users.config as config
from django.utils.translation import gettext_lazy as _
from django.core.validators import BaseValidator
import jsonschema
import django


class JSONSchemaValidator(BaseValidator):
    def compare(self, input, schema):
        try:
            jsonschema.validate(input, schema)
        except jsonschema.exceptions.ValidationError:
            raise django.core.exceptions.ValidationError(
                '%(value)s failed JSON schema check', params={'value': input})


def validate_no_news_source(value):
    if value not in config.NEWS_SITES:
        raise ValidationError(
            _('%(value)s is not an available news source'),
            params={'value': value},
        )
