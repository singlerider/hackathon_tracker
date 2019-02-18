from django.contrib import admin
from mentor_tracker.models import (Device, ExpertiseCategory, Location,
                                   Organization, Personnel,
                                   PersonnelExpertiseCategory,
                                   PersonnelDevice,
                                   PersonnelLocationEntry,
                                   PersonnelOrganization)


class PersonnelAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "username")


class PersonnelExpertiseCategoryAdmin(admin.ModelAdmin):
    search_fields = (
        "personnel__first_name", "personnel__last_name", "personnel__username",
        "expertise_category__category"
    )


class LocationAdmin(admin.ModelAdmin):
    search_fields = (
        "street_address", "building_number", "floor", "description"
    )


class OrganizationAdmin(admin.ModelAdmin):
    search_fields = (
        "street_address", "building_number", "floor", "description"
    )


class DeviceAdmin(admin.ModelAdmin):
    search_fields = ("make", "product", "version", "uuid")


class PersonnelOrganizationAdmin(admin.ModelAdmin):
    search_fields = (
        "personnel__first_name", "personnel__last_name", "personnel__username",
        "organization__name"
    )


class PersonnelDeviceAdmin(admin.ModelAdmin):
    search_fields = (
        "personnel__first_name", "personnel__last_name", "personnel__username",
        "device__make", "device__product", "device__version", "device__uuid",
        "tracked"
    )


class PersonnelLocationEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
    search_fields = (
        "personnel__first_name", "personnel__last_name", "personnel__username",
        "location__street_address", "location__building_number",
        "location__floor", "location__description", "signal_strength"
    )


admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(ExpertiseCategory)
admin.site.register(
    PersonnelExpertiseCategory, PersonnelExpertiseCategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(PersonnelOrganization, PersonnelOrganizationAdmin)
admin.site.register(PersonnelDevice, PersonnelDeviceAdmin)
admin.site.register(PersonnelLocationEntry, PersonnelLocationEntryAdmin)
