from django.db import models
from common.models import CommonModel


class CategoryKindChoices(models.TextChoices):
    ROOMS = "rooms", "Rooms"
    EXPERIENCES = "experiences", "Experiences"


class Category(CommonModel):

    """Room and Experience Category"""

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=20,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
