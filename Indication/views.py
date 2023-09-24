from django.shortcuts import render
from .models import Indication, InstalledMeteringDevice, PersonalAccount
from rest_framework.views import APIView

class IndicationController(APIView):
    def post(current_value, time_of_taking, account_number):
        indication = Indication.objects.create(current_value=current_value,
                                      time_of_taking=time_of_taking,
                                      metering_device=InstalledMeteringDevice.objects.get(personal_account=PersonalAccount.objects.get(account_number=account_number)))
        indication.save()
        print("Record saved successfully")