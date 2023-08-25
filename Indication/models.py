from django.db import models
from datetime import datetime

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
    number = models.IntegerField(max_length=10)
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
    phone_number = models.IntegerField(null=True, max_length=10)
    verification_code = models.TextField()
    code_validity = models.DateTimeField(default=datetime.now())

class InstalledMeteringDevice(models.Model):
    personal_account = models.ForeignKey(PersonalAccount, on_delete=models.CASCADE)
    metering_device = models.ForeignKey(MeteringDevice, on_delete=models.CASCADE)
    installation_date = models.DateField()
    remove_date =  models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ["personal_account","metering_device","installation_date"]

class Indication(models.Model):
    current_value = models.IntegerField(max_length=8)
    time_of_taking = models.DateTimeField()
    metering_device = models.ForeignKey(InstalledMeteringDevice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["current_value", "time_of_taking", "metering_device"]