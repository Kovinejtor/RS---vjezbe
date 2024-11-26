# 5. Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
# praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
# sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime ,
# broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
# prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina secure_data mora za
# svaki rječnik vratiti novi rječnik u obliku: {'prezime': prezime , 'broj_kartice': 'enkriptirano',
# 'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
# vrijednost ulaznog stringa.

import asyncio

async def secure_data(osjetljivi_podaci):
    await asyncio.sleep(3)
    
    enkriptirani_podaci = {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': str(hash(osjetljivi_podaci['broj_kartice'])),
        'CVV': str(hash(osjetljivi_podaci['CVV']))
    }
    
    return enkriptirani_podaci

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Peric', 'broj_kartice': '3932032434242344', 'CVV': '345'},
        {'prezime': 'Joric', 'broj_kartice': '9432834294329342', 'CVV': '436'},
        {'prezime': 'Zovic', 'broj_kartice': '9323932832932932', 'CVV': '123'}
    ]
    
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    enkriptirani_podaci = await asyncio.gather(*zadaci)
    
    for enkriptirani_podaci in enkriptirani_podaci:
        print(enkriptirani_podaci)

asyncio.run(main())
