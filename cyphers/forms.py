from django import forms
from .models import Cypher, Deck, DeckCypher


class CypherForm(forms.ModelForm):
    class Meta:
        model = Cypher
        fields = ['name', 'description', 'dice_qty', 'dice_type', 'mod']


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name']


class FillForm(forms.ModelForm):
    class Meta:
        model = DeckCypher
        fields = ['deck_id', 'cypher_id']
