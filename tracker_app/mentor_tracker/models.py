from django.db import models
from django.contrib.auth.models import AbstractUser


class Personnel(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    expertise_categories = models.ManyToManyField(
        "ExpertiseCategory", through="PersonnelExpertiseCategory")
    organizations = models.ManyToManyField(
        "Organization", through="PersonnelOrganization")
    devices = models.ManyToManyField("Device", through="PersonnelDevice")
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Personnel"


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


class Organization(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["description"])
        ]


class PersonnelOrganization(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        if self.personnel.first_name and self.personnel.last_name:
            return (
                f"{self.personnel.first_name} {self.personnel.last_name}, "
                f"{self.organization.name}"
            )
        return f"{self.personnel.username}, {self.organization.name}"


class Device(models.Model):
    make = models.CharField(max_length=40, help_text="Example: Apple")
    product = models.CharField(max_length=40, help_text="Example: Galaxy")
    version = models.CharField(max_length=40, help_text="Example: Xs Max")
    uuid = models.CharField(
        max_length=17, help_text="Example: 00:00:00:00:00:00", unique=True)

    def __str__(self):
        return f"{self.make} {self.product} {self.version}: {self.uuid}"

    class Meta:
        indexes = [
            models.Index(fields=["make"]),
            models.Index(fields=["product"]),
            models.Index(fields=["version"]),
            models.Index(fields=["uuid"])
        ]


class PersonnelDevice(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    tracked = models.BooleanField(default=True)

    def __str__(self):
        if self.personnel.first_name and self.personnel.last_name:
            return (
                f"{self.personnel.first_name} {self.personnel.last_name}, "
                f"{self.device.uuid}, Tracked: {self.tracked}"
            )
        return (
            f"{self.personnel.username}, {self.device.uuid}, "
            f"Tracked: {self.tracked}"
        )

    class Meta:
        unique_together = ("personnel", "device",)
        indexes = [
            models.Index(fields=["personnel", "device"]),
            models.Index(fields=["personnel"]),
            models.Index(fields=["device"]),
            models.Index(fields=["tracked"])
        ]


class PersonnelLocationEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    signal_strength = models.IntegerField()

    def __str__(self):
        if self.personnel.first_name and self.personnel.last_name:
            return (
                f"{self.timestamp} - "
                f"{self.personnel.first_name} {self.personnel.last_name}, "
                f"{self.location.street_address}, "
                f"building: {self.location.building_number}, "
                f"floor: {self.location.floor}, "
                f"signal strength: {self.signal_strength}"
            )
        return (
            f"{self.timestamp} - "
            f"{self.personnel.username}"
            f"{self.location.street_address}, "
            f"building: {self.location.building_number}, "
            f"floor: {self.location.floor}, "
            f"signal strength: {self.signal_strength}"
        )

    class Meta:
        verbose_name_plural = "Personnel location entries"
        indexes = [
            models.Index(fields=["personnel"]),
            models.Index(fields=["location"]),
            models.Index(fields=["timestamp"]),
            models.Index(fields=["-timestamp"]),
            models.Index(fields=["personnel", "location"]),
            models.Index(fields=["personnel", "location", "signal_strength"]),
            models.Index(fields=["personnel", "location", "timestamp"])
        ]
