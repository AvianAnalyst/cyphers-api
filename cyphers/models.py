from django.db import models


# Create your models here.
class Cypher(models.Model):
    D = 'd%'
    D4 = 'd1'
    D6 = 'd1'
    D8 = 'd1'
    D10 = 'd1'
    D12 = 'd1'
    D20 = 'd1'
    DICE_TYPE= [
        (D4, 'd4'),
        (D6, 'd6'),
        (D8, 'd8'),
        (D10, 'd10'),
        (D12, 'd12'),
        (D20, 'd20'),
        (D, 'Percentile'),
    ]
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    dice_type = models.CharField(
        max_length=2,
        choices=DICE_TYPE,
    )
    dice_qty = models.IntegerField()
    mod = models.IntegerField()

    def __str__(self):
        return self.name


class Deck(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeckCypher(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    cypher_id = models.ForeignKey(Cypher, on_delete=models.CASCADE)

