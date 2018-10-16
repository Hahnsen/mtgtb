# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from models import CardType, Color, Card
import re

# Register your models here.


class CardTypeAdmin(admin.ModelAdmin):
    """Admin for CardType."""
    fields = ['name', 'speed']
    list_display = ['name', 'speed']



class CardForm(forms.ModelForm):
    """Form for the cards."""
    class Meta:
        """Model to use."""
        model = Card
        exclude = ()
        widgets = {
            'colors': forms.CheckboxSelectMultiple()}

    def _check_manacost(self, data):
        """Check if manacost is entered correctly."""
        manacost = data.get("manacost")
        valid = re.compile('^[0-9]*(W|U|R|B|G)*$')
        if valid.match(manacost) is None:
            raise ValidationError("Please enter manacost in correct format, " +
                                  "e.g. '3WURR' (number for mana of any color "
                                  "+ capital color letters expressing the " +
                                  "mana symbols on the card).")

    def clean(self):
        """Verify."""
        cleaned_data = super(CardForm, self).clean()
        self._check_manacost(cleaned_data)
        return cleaned_data

    
class CardAdmin(admin.ModelAdmin):
    """Admin for Card."""
    form = CardForm
    search_fields = ['name']
    list_display = ['name', 'cardtype', 'manacost']


admin.site.register(Color)
admin.site.register(CardType, CardTypeAdmin)
admin.site.register(Card, CardAdmin)
