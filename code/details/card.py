class Card:
    card_number: str
    card_holder_name: str
    expiry_date: str
    cvv: str

    def __init__(self, 
                 card_number, 
                 card_holder_name, 
                 expiry_date, 
                 cvv):
        
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.expiry_date = expiry_date
        self.cvv = cvv