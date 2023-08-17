from django.contrib import admin
from .models import Indication, PersonalAccount, MeteringDevice, MeterModel, Manufacturer, InstalledMeteringDevice

admin.site.register(Indication)
admin.site.register(PersonalAccount)
admin.site.register(InstalledMeteringDevice)
admin.site.register(Manufacturer)
admin.site.register(MeterModel)
admin.site.register(MeteringDevice)