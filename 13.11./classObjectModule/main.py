from shop.proizvodi import dodaj_proizvod, proizvodi
from shop.narudzbe import napravi_narudzbu

novi_proizvodi = [
{"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
{"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in novi_proizvodi:
    dodaj_proizvod(proizvod)

for proizvod in proizvodi:
    print(proizvod.ispis())

narudzba_data = [
    {"naziv": "Miš", "cijena": 5000, "kolicina": 21},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 3}
]

narudzba = napravi_narudzbu(narudzba_data)
if narudzba:
    print(narudzba.ispis_narudzbe())
