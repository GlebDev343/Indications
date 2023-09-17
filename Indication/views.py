from django.shortcuts import render
from .models import Indication, MeteringDevice
from rest_framework import APIView

class IndicationController(APIView):
    def post(current_value, time_of_taking, account_number):
        indication = Indication.objects.create(current_value=current_value,
                                      time_of_taking=time_of_taking,
                                      metering_device=MeteringDevice.objects.find(number=metering_device))
        indication.save()
        print("Record saved successfully")