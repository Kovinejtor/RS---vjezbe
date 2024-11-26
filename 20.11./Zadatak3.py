# 3. Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
# poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
# od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
# imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
# provjera traje 3 sekunde.
baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]
# Ako se korisnik ne nalazi u bazi, vratite poruku "Korisnik {korisnik} nije pronađen."
# Ako se korisnik nalazi u bazi, potrebno je pozvati vanjsku korutinu autorizacija() koja će simulirati
# autorizaciju korisnika u trajanju od 2 sekunde. Funkcija kao ulazni parametar prima rječnik korisnika iz baze
# i lozinku proslijeđenu iz korutine autentifikacija() . Autorizacija simulira dekripciju lozinke (samo
# provjerite podudaranje stringova) i provjeru s lozinkom iz baze_lozinka. Ako su lozinke jednake, korutine
# vraća poruku "Korisnik {korisnik}: Autorizacija uspješna." , a u suprotnom "Korisnik
# {korisnik}: Autorizacija neuspješna." .
baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]
# Korutinu autentifikacija() pozovite u main() funkciji s proizvoljnim korisnikom i lozinkom.

import asyncio
from asyncio.tasks import sleep
async def autentifikacija(korisnik): 
    await asyncio.sleep(3)
    if any(k['korisnicko_ime'] == korisnik['korisnicko_ime'] and k['email'] == korisnik['email'] for k in baza_korisnika):
        await autorizacija(korisnik) 
    else:
        print(f"Korisnik {korisnik} nije pronaden.")

async def autorizacija(korisnik):
    await asyncio.sleep(2)
    if any(k['korisnicko_ime'] == korisnik['korisnicko_ime'] and k['lozinka'] == korisnik['lozinka'] for k in baza_lozinka):
        print(f"Korisnik {korisnik}: Autorizacija uspješna.")

    else:
        "Korisnik {korisnik}: Autorizacija neuspješna."


async def main():
    korisnik = {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'super_teska_lozinka'}
    await autentifikacija(korisnik)

asyncio.run(main())

