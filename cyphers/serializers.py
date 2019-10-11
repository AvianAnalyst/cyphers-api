from .models import Cypher, Deck
from rest_framework import serializers


class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = ['name', 'cyphers']


class CypherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cypher
        fields = ['name', 'description', 'dice_qty', 'dice_type', 'mod', 'decks']
