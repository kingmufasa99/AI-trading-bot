class Portfolio:
    """Classe simulant la gestion du portefeuille."""


    def __init__(self):
        # Un dictionnaire pour stocker les positions : clé = symbole, valeur = quantité

        self.positions = {}

    def invested(self, symbol):
        """Retourne True si une position sur 'symbol' existe."""

        symbol = symbol.upper()
        return self.positions.get(symbol, 0) > 0

    def add_position(self, symbol, quantity):
        """Ajoute une position (pour simulation)."""

        symbol = symbol.upper()
        self.positions[symbol] = self.positions.get(symbol, 0) + quantity