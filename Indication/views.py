from django.shortcuts import render
from .models import Indication, InstalledMeteringDevice, PersonalAccount, max_current_value_validator
from rest_framework.views import APIView

class IndicationController(APIView):
    def post(current_value, time_of_taking, account_number):
        personal_account = PersonalAccount.objects.get(account_number=account_number)
        installed_metering_device = InstalledMeteringDevice.objects.get(personal_account=personal_account)
        indication = Indication(current_value=current_value,
                                time_of_taking=time_of_taking,
                                installed_metering_device=installed_metering_device)

        max_current_value_validator(int(indication.current_value))
        indication.save()
        print("Record saved successfully")
