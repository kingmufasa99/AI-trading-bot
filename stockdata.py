class StockData:
    """
    Classe représentant les données d'un titre.
    Dans cet exemple, les valeurs sont fixes pour la démonstration.
    """
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.bid = 145.18
        self.ask = 145.21
        self.volume = 86473580.0

    def __str__(self):
        return f"{self.symbol} - Bid: {self.bid}, Ask: {self.ask}, Volume: {self.volume}"