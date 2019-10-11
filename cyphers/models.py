from django.db import models


# Create your models here.
class Cypher(models.Model):
    D4 = 'd1'
    D6 = 'd2'
    D8 = 'd3'
    D10 = 'd4'
    D12 = 'd5'
    DICE_TYPE = [
        (D4, 'd4'),
        (D6, 'd6'),
        (D8, 'd8'),
        (D10, 'd10'),
        (D12, 'd12'),
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
    cyphers = models.ManyToManyField(Cypher, related_name='decks')

    def __str__(self):
        return self.name
