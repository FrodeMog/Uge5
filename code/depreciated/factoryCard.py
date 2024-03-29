from details.card import Card
from factories.factory import Factory

class FactoryCard(Factory):
    def __init__(self):
        pass

    def create_card(self, card_data=None, **kwargs):
        if card_data is None:
            card_data = kwargs
        else:
            card_data.update(kwargs)

        card = super().create(Card, **card_data)

        return card