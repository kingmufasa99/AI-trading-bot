from datetime import datetime


class Notification:
    """Classe permettant de récupérer les notifications."""

    current_dateTime = datetime.now()

    @staticmethod
    def get_notifications(n, current_dateTime):
        """
        Retourne une liste de n notifications.
        Chaque notification est représentée par une liste [heure, titre, message].
        """

        dummy_notifications = [
            [f"{current_dateTime}", "Level 2", "You are not authorized for symbol: AMD"],
            [f"{current_dateTime}", "Error", "You are not authorized for symbol: AMD"],
            [f"{current_dateTime}", "You are not authorized for symbol: AAPL"],
        ]
        return dummy_notifications[:n]