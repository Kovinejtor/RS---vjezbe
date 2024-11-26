# 2. Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
# listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
# korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
# sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
# se mora izvršavati ~5 sekundi.

import asyncio
async def fetch_user(): 
    baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
    await asyncio.sleep(3)
    return baza_korisnika 

async def fetch_thing(): 
    thing = [
    {'thing': 'phone', 'price': '13eu'},
    {'thing': 'iphone', 'price': '12eu'},
    {'thing': 'book', 'price': '16eu'},
    {'thing': 'laptop', 'price': '10eu'}
    ]
    await asyncio.sleep(5)
    return thing 

async def main():
    korisnici, stvari = await asyncio.gather(fetch_user(), fetch_thing())
    print("Podaci o korisnicima: ", korisnici)
    print("Podaci o stvarima: ", stvari)

asyncio.run(main())

