from django.db import models

class Manufacturer(models.Model):
    name = models.CharField()
    contact_details = models.CharField()

class MeterModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField()
    scale_size = models.IntegerField()

class MeteringDevice(models.Model):
    number = models.IntegerField()
    model_metering_device = models.ForeignKey(MeterModel, on_delete=models.CASCADE)
    date_of_issue = models.DateField()

class Indication(models.Model):
    current_value = models.IntegerField()
    time_of_taking = models.DateTimeField()
    metering_device = models.ForeignKey(MeteringDevice, on_delete=models.CASCADE)

class PersonalAccount(models.Model):
    address = models.CharField()
    account_number = models.IntegerField()
    credentials = models.CharField()
    phone_number = models.IntegerField()

class InstalledMeteringDevice(models.Model):
    personal_account = models.ForeignKey(PersonalAccount, on_delete=models.CASCADE)
    metering_device = models.ForeignKey(MeteringDevice, on_delete=models.CASCADE)
    installation_date = models.DateField()
    remove_date =  models.DateField(null=True)