from rest_framework import viewsets
from .models import Cypher, Deck
from .serializers import DeckSerializer, CypherSerializer


# Create your views here.
class DeckViewSet(viewsets.ModelViewSet):
        queryset = Deck.objects.all().prefetch_related('cyphers').order_by('name')
        serializer_class = DeckSerializer


class CypherViewSet(viewsets.ModelViewSet):
        queryset = Cypher.objects.all().prefetch_related('decks').order_by('name')
        serializer_class = CypherSerializer
# def make_cypher(request):
#     if request.method == 'POST':
#         form = CypherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = 'success!'
#         else:
#             msg = 'Failure'
#     else:
#         msg = None
#         form = CypherForm()
#     cyphers = Cypher.objects.all()
#
#     return render(request, 'card.html', {'form': form, 'msg': msg, 'cyphers': cyphers})
#
#
# def make_deck(request):
#     if request.method == 'POST':
#         form = DeckForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = 'success!'
#         else:
#             msg = 'Failure'
#     else:
#         msg = None
#         form = DeckForm()
#     decks = Deck.objects.all()
#
#     return render(request, 'deck.html', {'form': form, 'msg': msg, 'decks': decks})
#
#
# def fill_deck(request):
#     if request.method == 'POST':
#         form = FillForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = 'success!'
#         else:
#             msg = 'failure!'
#     else:
#         msg = None
#         form = FillForm()
#     decks = {}
#     deck_names = Deck.objects.all().values('name', )
#     # for deck in deck_names:
#     #     decks[deck] = DeckCypher.objects.filter(deck_id=)
#     # cyphers = Cypher.objects.all()
#
#     return render(request, 'fill.html', {'form': form, 'msg': msg, 'decks': decks})
