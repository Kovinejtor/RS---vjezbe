from .proizvodi import proizvodi 

class Narudzba:
    def __init__(self, proizvodi):
        self.proizvodi = proizvodi
        self.ukupna_cijena = sum(p["cijena"] * p["kolicina"] for p in proizvodi)

    def ispis_narudzbe(self):
        naruceni_proizvodi = ", ".join([f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi])
        return f"Naruceni proizvodi: {naruceni_proizvodi}, ukupna cijena: {self.ukupna_cijena} eur"

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        print("Argument 'proizvodi' mora biti lista")
        return None
    if len(lista_proizvoda) == 0:
        print("Lista ne smije biti prazna")
        return None
    if not all(isinstance(p, dict) for p in lista_proizvoda):
        print("Svi elementi u listi moraju biti rjecnici")
        return None
    if not all("naziv" in p and "cijena" in p and "kolicina" in p for p in lista_proizvoda):
        print("Svaki rjecnik mora sadrzavati kljuceve 'naziv', 'cijena' i 'kolicina'")
        return None

    for p in lista_proizvoda:
        proizvod = next((prod for prod in proizvodi if prod.naziv == p["naziv"]), None)
        if not proizvod or proizvod.kolicina < p["kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan")
            return None

    for p in lista_proizvoda:
        proizvod = next(prod for prod in proizvodi if prod.naziv == p["naziv"])
        proizvod.kolicina -= p["kolicina"]

    return Narudzba(lista_proizvoda)
