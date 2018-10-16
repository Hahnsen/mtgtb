# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CardType(models.Model):
    """The card type of each card."""

    SPEED_CHOICES = (
        ('S', 'sorcery'),
        ('I', 'instant'))

    name = models.CharField(max_length=20, null=False, unique=True)
    speed = models.CharField(max_length=1,
                             choices=SPEED_CHOICES)

    def __unicode__(self):
        """Return unicode representaion of name."""
        return u"{}".format(self.name)


class Color(models.Model):
    """The colors available in mtg."""

    COLOR_CHOICES = (
        ('white', 'W'),
        ('blue', 'U'),
        ('black', 'B'),
        ('green', 'G'),
        ('red', 'R'),
        ('colorless', 'C'))

    name = models.CharField(max_length=1,
                            choices=COLOR_CHOICES,
                            unique=True)

    def __unicode__(self):
        """Return unicode representation of name."""
        return u"{}".format(self.name)


class Card(models.Model):
    """Class for each individual card."""

    name = models.CharField(max_length=40)
    manacost = models.CharField(max_length=40)
    #converted_manacost = models.PositiveIntegerField()

    # Foreign Keys
    cardtype = models.ForeignKey(CardType,
                                 on_delete=models.PROTECT)

    # ManyToMany Fields:
    colors = models.ManyToManyField(Color)

    def __unicode__(self):
        return u"{}".format(self.name)
