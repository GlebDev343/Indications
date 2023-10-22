import pytest
from django.core.exceptions import ValidationError
from .models import phone_value_validator, max_current_value_validator
from .models import (
    Indication,
    InstalledMeteringDevice,
    PersonalAccount,
    MeteringDevice,
    Manufacturer,
    MeterModel,
)


@pytest.mark.django_db
def test_correct_max_value_validation():
    manufacturer = Manufacturer(name="manufacturer1")
    meter_model = MeterModel(
        manufacturer=manufacturer, model_name="model1", scale_size=9
    )
    metering_device = MeteringDevice(
        number=1, model_metering_device=meter_model, date_of_issue="2000-01-01"
    )
    personal_account = PersonalAccount(
        address="address1",
        account_number=1,
        first_name="fname",
        patronymic="patronymic",
        last_name="lname",
        verification_code="QWERTY",
    )
    installed_metering_device = InstalledMeteringDevice(
        personal_account=personal_account,
        metering_device=metering_device,
        installation_date="2002-02-02",
    )
    indication = Indication(
        current_value=123456,
        time_of_taking="2003-03-03 00:00:00",
        metering_device=installed_metering_device,
    )
    assert max_current_value_validator(indication.current_value) == None


@pytest.mark.django_db
def test_uncorrect_max_value_validation():
    manufacturer = Manufacturer(name="manufacturer1")
    meter_model = MeterModel(
        manufacturer=manufacturer, model_name="model1", scale_size=9
    )
    metering_device = MeteringDevice(
        number=1, model_metering_device=meter_model, date_of_issue="2000-01-01"
    )
    personal_account = PersonalAccount(
        address="address1",
        account_number=1,
        first_name="fname",
        patronymic="patronymic",
        last_name="lname",
        verification_code="QWERTY",
    )
    installed_metering_device = InstalledMeteringDevice(
        personal_account=personal_account,
        metering_device=metering_device,
        installation_date="2002-02-02",
    )
    indication = Indication(
        current_value=1234567,
        time_of_taking="2003-03-03 00:00:00",
        metering_device=installed_metering_device,
    )

    with pytest.raises(ValidationError):
        max_current_value_validator(indication.current_value)


@pytest.mark.django_db
def test_phone_less_than_required():
    personal_account = PersonalAccount(
        address="address1",
        account_number=1,
        first_name="fname",
        patronymic="patronymic",
        last_name="lname",
        verification_code="QWERTY",
        phone_number=1234567, 
    )

    with pytest.raises(ValidationError):
        phone_value_validator(personal_account.phone_number)


@pytest.mark.django_db
def test_phone_greater_than_required():
    personal_account = PersonalAccount(
        address="address1",
        account_number=1,
        first_name="fname",
        patronymic="patronymic",
        last_name="lname",
        verification_code="QWERTY",
        phone_number=12345678910, 
    )

    with pytest.raises(ValidationError):
        phone_value_validator(personal_account.phone_number)


@pytest.mark.django_db
def test_phone_normal_length():
    personal_account = PersonalAccount(
        address="address1",
        account_number=1,
        first_name="fname",
        patronymic="patronymic",
        last_name="lname",
        verification_code="QWERTY",
        phone_number=123456789, 
    )

    assert phone_value_validator(personal_account.phone_number) == None
