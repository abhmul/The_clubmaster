from django.db import models


class Organization(models.Model):
    """
    The model representation of an Organization.
    """

    name = models.CharField(max_length=30)
    website = models.URLField(blank=True)
    logo = models.ImageField(blank=True)
    contact = models.EmailField()
    description = models.CharField(max=140)

