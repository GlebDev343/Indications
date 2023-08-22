from django.contrib import admin
from .models import Indication, PersonalAccount, MeteringDevice, MeterModel, Manufacturer, InstalledMeteringDevice

class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Indication, DeleteNotAllowedModelAdmin)
admin.site.register(PersonalAccount, DeleteNotAllowedModelAdmin)
admin.site.register(InstalledMeteringDevice, DeleteNotAllowedModelAdmin)
admin.site.register(Manufacturer, DeleteNotAllowedModelAdmin)
admin.site.register(MeterModel, DeleteNotAllowedModelAdmin)
admin.site.register(MeteringDevice, DeleteNotAllowedModelAdmin)