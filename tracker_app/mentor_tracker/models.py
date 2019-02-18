from django.db import models
from django.contrib.auth.models import AbstractUser


class Personnel(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    expertise_categories = models.ManyToManyField(
        "ExpertiseCategory", through="PersonnelExpertiseCategory")


class ExpertiseCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Expertise categories"


class PersonnelExpertiseCategory(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    expertise_category = models.ForeignKey(
        ExpertiseCategory, on_delete=models.CASCADE)
    search_fields = [
        "personnel__username", "personnel__first_name",
        "personnel__last_name"
    ]

    def __str__(self):
        if self.personnel.first_name and self.personnel.last_name:
            return (
                f"{self.personnel.first_name} {self.personnel.last_name}, "
                f"{self.expertise_category.category}"
            )
        return f"{self.personnel.username}, {self.expertise_category.category}"

    class Meta:
        verbose_name_plural = "Personnel expertise categories"
        unique_together = ("personnel", "expertise_category",)
        indexes = [
            models.Index(fields=["personnel", "expertise_category"]),
            models.Index(fields=["personnel"]),
            models.Index(fields=["expertise_category"])
        ]


class Location(models.Model):
    street_address = models.TextField(null=False)
    building_number = models.CharField(max_length=20, null=True)
    floor = models.CharField(max_length=15, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        if not self.building_number or not self.floor:
            return self.street_address
        return (
            f"{self.street_address}, building: {self.building_number}, "
            f"floor: {self.floor}"
        )

    class Meta:
        indexes = [
            models.Index(fields=["street_address"]),
            models.Index(fields=["building_number"]),
            models.Index(fields=["floor"]),
            models.Index(fields=["description"])
        ]
