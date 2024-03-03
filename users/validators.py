import re


def validate_phone(phone):
    return phone.isdigit()


def validate_class(_class):
    return bool(re.match(r'\d{1,2}[А-Яа-я[^ЙиЪъЬь]]+', _class))


def validate_age(age):
    return age < 100
