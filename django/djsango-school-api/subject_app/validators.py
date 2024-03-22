from django.core.exceptions import ValidationError
import re


def validate_subject_format(subject):
    error_message = "Subject must be in title case format."
    regex = r'^[A-Z][a-z]+[ [A-Za-z][a-z]*]*$'
    good_subject = re.match(regex, subject)
    if good_subject:
        return subject
    else:
        raise ValidationError(error_message)


def validate_professor_name(name):
    error_message = 'Professor name must be in the format "Professor Adam".'
    regex = r'^[A-Z][a-z\.]+[ [A-Z][a-z]*]*$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message)
