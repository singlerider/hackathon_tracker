from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Personnel(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()


class ExpertiseCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Expertise categories"
