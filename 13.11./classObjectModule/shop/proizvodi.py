class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        return f"Proizvod: {self.naziv}, cijena: {self.cijena}, kolicina: {self.kolicina}"

proizvodi = [
    Proizvod("Toster", 31, 2),
    Proizvod("Marmelada", 6, 4)
]

def dodaj_proizvod(novi_proizvod):
    proizvodi.append(Proizvod(novi_proizvod["naziv"], novi_proizvod["cijena"], novi_proizvod["kolicina"]))
