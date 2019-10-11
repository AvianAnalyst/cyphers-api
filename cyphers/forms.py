from django import forms
from .models import Cypher, Deck


class CypherForm(forms.ModelForm):
    class Meta:
        model = Cypher
        fields = ['name', 'description', 'dice_qty', 'dice_type', 'mod', 'decks']


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name', 'cyphers']
