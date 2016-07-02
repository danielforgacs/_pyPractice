import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQLA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__():
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
        pass

    def __getitem__(self, position):
        return self._cards[position]