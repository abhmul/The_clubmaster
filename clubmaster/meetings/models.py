from django.db import models


class Meeting(models.Model):
    """
    This is a model that represents a Meeting.
    """

    date = models.DateTimeField()
    name = models.CharField(max_length=24)
    files = models.ManyToManyField(MeetingFile)


class MeetingFile(models.Model):
    """
    This is model for a meeting file.
    """

    name = models.CharField(max_length=24)
    file = models.FileField()
