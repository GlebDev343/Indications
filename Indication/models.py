import datetime
from datetime import timedelta
from django.db import models
from django.core.exceptions import ValidationError

def min_phone_value(value):
    if value < 10000000:
        raise ValidationError(f"{value} is less than required.")

def max_current_value(value):
    if value > 999999:
        raise ValidationError(f"{value} is greater than required.")

class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    contact_details = models.CharField()

class MeterModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField()
    scale_size = models.IntegerField()

    class Meta:
        unique_together = ["manufacturer","model_name"]

class MeteringDevice(models.Model):
    number = models.IntegerField()
    model_metering_device = models.ForeignKey(MeterModel, on_delete=models.CASCADE)
    date_of_issue = models.DateField()

    class Meta:
        unique_together = ["number","model_metering_device","date_of_issue"]

class PersonalAccount(models.Model):
    address = models.CharField()
    account_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, validators=[min_phone_value])
    verification_code = models.CharField()
    code_validity = models.DateTimeField(default="1900-01-01 00:00:00")

class InstalledMeteringDevice(models.Model):
    personal_account = models.ForeignKey(PersonalAccount, on_delete=models.CASCADE)
    metering_device = models.ForeignKey(MeteringDevice, on_delete=models.CASCADE)
    installation_date = models.DateField()
    remove_date =  models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ["personal_account","metering_device","installation_date"]

class Indication(models.Model):
    current_value = models.IntegerField(validators=[max_current_value])
    time_of_taking = models.DateTimeField()
    metering_device = models.ForeignKey(InstalledMeteringDevice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["metering_device", "current_value", "time_of_taking"]