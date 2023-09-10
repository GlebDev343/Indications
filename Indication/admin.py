from django.contrib import admin
from .models import Indication, PersonalAccount, MeteringDevice, MeterModel, Manufacturer, InstalledMeteringDevice

class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

class PersonalAccountAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(PersonalAccountAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['code_validity'].required = False
        return form
    
    def has_delete_permission(self, request, obj=None):
        return False

class InstalledMeteringDeviceAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(InstalledMeteringDeviceAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['remove_date'].required = False
        return form
    
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Indication, DeleteNotAllowedModelAdmin)
admin.site.register(PersonalAccount, PersonalAccountAdmin)
admin.site.register(InstalledMeteringDevice, InstalledMeteringDeviceAdmin)
admin.site.register(Manufacturer, DeleteNotAllowedModelAdmin)
admin.site.register(MeterModel, DeleteNotAllowedModelAdmin)
admin.site.register(MeteringDevice, DeleteNotAllowedModelAdmin)