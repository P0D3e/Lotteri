import random

class Lotteri:
    def __init__(self):
        self.list_vinster = [
            "Ett kilo fjädrar",
            "Bugatti veiron",
            "Karta över norderön",
            "Ockelbo 500",
            "10 liter mangojuice",
            "Prada keps",
            "Versace Väska",
            "Minttu flaska",
            "Cross",
            "Ett paket strumpor",
            "Resa till Colombia",
            "En afrikansk katt",
            "Oboy Pulver",
            "En RHIB båt",
            "En valfri telefon",
            "En personlig butler",
            "En cubansk tiger",
            "Parfume de Marley",
            "Konsertbiljett till Metallica",
            "En turkisk gris",
            "En flodhäst",
        ]

    def get_vinst(self):
        slumptal = random.randint(0, 19)
        return self.list_vinster[slumptal]
