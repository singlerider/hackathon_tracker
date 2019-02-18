from django.contrib import admin
from mentor_tracker.models import (Device, ExpertiseCategory, Location,
                                   Organization, Personnel,
                                   PersonnelExpertiseCategory,
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


admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(ExpertiseCategory)
admin.site.register(
    PersonnelExpertiseCategory, PersonnelExpertiseCategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(PersonnelOrganization, PersonnelOrganizationAdmin)
