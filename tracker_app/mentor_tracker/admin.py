from django.contrib import admin
from mentor_tracker.models import (ExpertiseCategory, Personnel,
                                   PersonnelExpertiseCategory)


class PersonnelAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "username")


class PersonnelExpertiseCategoryAdmin(admin.ModelAdmin):
    search_fields = (
        "personnel__first_name", "personnel__last_name", "personnel__username",
        "expertise_category__category"
    )


admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(ExpertiseCategory)
admin.site.register(
    PersonnelExpertiseCategory, PersonnelExpertiseCategoryAdmin)
