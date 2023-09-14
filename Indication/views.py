from django.shortcuts import render
from .models import Indication, MeteringDevice
from rest_framework import APIView

class IndicationController(APIView):
    current_value = None
    time_of_taking = None
    metering_device = None

    def post():
        indication = Indication.objects.create(current_value=current_value,
                                      time_of_taking=time_of_taking,
                                      metering_device=MeteringDevice.objects.find(number=metering_device))
        indication.save()
        print("Record saved successfully")