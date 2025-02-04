import yfinance as yf

class StockData:
    """
    Classe représentant les données en temps réel d'un titre.
    Utilise l'API Yahoo Finance via la librairie yfinance pour obtenir le prix actuel.
    """
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.refresh()

    def _fetch_data(self):
        ticker = yf.Ticker(self.symbol)
        info = ticker.info
        self.current_price = info.get("regularMarketPrice")
        self.bid = info.get("bid")
        self.ask = info.get("ask")
        self.volume = info.get("volume")

    def refresh(self):
        """Rafraîchit les données en temps réel."""
        self._fetch_data()

    def __str__(self):
        return (
            f"{self.symbol} - Price: {self.current_price}, "
            f"Bid: {self.bid}, Ask: {self.ask}, Volume: {self.volume}"
        )
