
# Find pylint codes at: http://pylint-messages.wikidot.com/all-codes
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=superfluous-parens

from django.db import models

# Create your models here.

class Rider(models.Model):
    plaque = models.CharField(max_length=4)
    startgroup = models.CharField(max_length=1)
    firstname = models.CharField(max_length=22)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    country = models.CharField(max_length=2)
    club = models.CharField(max_length=39)
    velo = models.CharField(max_length=2)
    time = models.CharField(max_length=5)


class Control(models.Model):
    seq = models.IntegerField()
    name = models.CharField(max_length=20)
    distance = models.IntegerField()
    inbound = models.BooleanField()

class Timestamp(models.Model):
    plaque = models.CharField(max_length=4)
    location = models.ForeignKey('Control', on_delete=models.CASCADE)
    timestamp = models.FloatField()
