from tradezero_api import TradeZero
from order import Order
from portfolio import Portfolio
from notification import Notification
from stockdata import StockData


class TradeZero:
    """
    Classe principale pour interagir avec la plateforme TradeZero.
    Cette classe gère la connexion, la récupération des données et l'exécution des ordres.
    """

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self._logged_in = False

        # Instanciation des objets Portfolio et Notification
        self.Portfolio = Portfolio()
        self.Notification = Notification

    def login(self):
        """Simule la connexion à la plateforme."""
        print(f"[TradeZero] Tentative de connexion pour l'utilisateur {self.user_name}...")
        # Ici, vous feriez la logique de connexion (par exemple avec Selenium)
        self._logged_in = True
        print("[TradeZero] Connexion réussie.")

    def conn(self):
        """Vérifie si la connexion est active."""
        if self._logged_in:
            print("[TradeZero] La connexion est active.")
        else:
            print("[TradeZero] Non connecté. Veuillez vous connecter d'abord avec login().")

    def data(self, symbol):
        """
        Retourne un objet StockData pour le symbole donné.
        Permet d'accéder aux propriétés telles que bid, ask, volume, etc.
        """
        return StockData(symbol)

    def market_order(self, order_type, symbol, quantity):
        """Place un ordre au marché."""
        print(f"[TradeZero] Ordre marché: {order_type} {quantity} actions de {symbol.upper()}.")

    def limit_order(self, order_type, symbol, quantity, limit_price):
        """Place un ordre à cours limité."""
        print(f"[TradeZero] Ordre limite: {order_type} {quantity} actions de {symbol.upper()} à {limit_price}.")

    def locate_stock(self, symbol, quantity, max_price):
        """Localise des actions (simulation)."""
        print(f"[TradeZero] Recherche de {quantity} actions de {symbol.upper()} avec un prix maximum de {max_price}.")

    def credit_locates(self, symbol):
        """Crédite les actions localisées (simulation)."""
        print(f"[TradeZero] Créditation des actions localisées pour {symbol.upper()}.")

    def exit(self):
        """Ferme la session et termine le driver."""
        print("[TradeZero] Fermeture de la session et arrêt du driver.")
        self._logged_in = False

    @property
    def bid(self):
        """Retourne le bid du titre actuellement affiché."""
        return self.data(self.current_symbol()).bid

    @property
    def ask(self):
        """Retourne l'ask du titre actuellement affiché."""
        return self.data(self.current_symbol()).ask

    @property
    def last(self):
        """Retourne la dernière valeur de transaction."""
        # Vous pouvez également implémenter ce calcul via self.data(...)
        return 145.00

    def current_symbol(self):
        """
        Retourne le symbole du titre actuellement affiché dans le panneau supérieur.
        Pour la simulation, on retourne un symbole fixe.
        """
        return "AAPL"


# Exemple d'utilisation
if __name__ == "__main__":
    # Création de la connexion TradeZero
    tz = TradeZero(user_name="mon_user", password="mon_password")
    tz.login()
    tz.conn()

    # Récupération des données pour AAPL
    aapl = tz.data("AAPL")
    print(f"Stock: {aapl.symbol},  Bid: {aapl.bid}, Ask: {aapl.ask}, Volume: {aapl.volume}")

    # Passage d'un ordre de vente à découvert sur AAPL
    tz.market_order(Order.BUY, "AAPL", 200)

    # Vérification du portefeuille et passage d'un ordre limite si non investi sur AMD
    if not tz.Portfolio.invested("AMD"):
        limit_price = tz.data("AMD").ask + 0.02
        tz.limit_order(Order.BUY, "AMD", 100, limit_price)
        # Simulation : ajout d'une position dans le portefeuille
        tz.Portfolio.add_position("AMD", 100)

    # Localisation et créditation d'actions
    while True:
        try:
            max_price = float(input("Entrez le prix maximum souhaité : "))
            break
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre réel.")

    tz.locate_stock("uber", 100, max_price)
    tz.credit_locates("uber")

    # Accès rapide aux propriétés bid, ask, last
    print(f"Bid rapide: {tz.bid}, Ask rapide: {tz.ask}, Last rapide: {tz.last}")

    # Vérification du symbole courant avant d'accéder à tz.bid
    symbol = "AAPL"
    if tz.current_symbol() == symbol.upper():
        print(f"Le bid pour {symbol.upper()} est: {tz.bid}")

    # Fermeture de la session
    tz.exit()
