import pytest
from django.core.exceptions import ValidationError
from .models import max_current_value
from .models import min_phone_value

@pytest.mark.django_db
def test_correct_max_value_validation():
    max_current_value(123456)

@pytest.mark.django_db
def test_uncorrect_max_value_validation():
    try:
        max_current_value(123456)
    except ValidationError:
        pass

@pytest.mark.django_db
def test_correct_min_phone_value_validation():
    min_phone_value(1234567890)

@pytest.mark.django_db
def test_uncorrect_min_phone_value_validation():
    try:
        min_phone_value(12345)
    except ValidationError:
        pass
