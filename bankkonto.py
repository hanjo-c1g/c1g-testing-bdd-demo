class Bankkonto:
    def __init__(self, startguthaben=0):
        self.guthaben = startguthaben

    def einzahlen(self, betrag):
        self.guthaben += betrag

    def abheben(self, betrag):
        if betrag > self.guthaben:
            return False  # Abhebung nicht möglich
        self.guthaben -= betrag
        return True
