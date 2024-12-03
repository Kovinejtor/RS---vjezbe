# Zadatak 5: Proizvodi i ruta za narudžbe
# Nadogradite poslužitelj iz prethodnog zadatka na način da podržava i POST metodu na putanji /narudzbe .
# Ova ruta prima JSON podatke o novoj narudžbu u sljedećem obliku. Za početak predstavite da je svaka
# narudžba jednostavna i sadrži samo jedan proizvod i naručenu količinu:
#{
# "proizvod_id": 1,
# "kolicina": 2
#}
# Handler korutina ove metode mora provjeriti postoji li proizvod s traženim ID-em unutar liste proizvodi .
# Ako ne postoji, vratite odgovor s statusom 404 i porukom {'error': 'Proizvod s traženim ID-em ne
# postoji'} . Ako proizvod postoji, dodajte novu narudžbu u listu narudžbi i vratite odgovor s nadopunjenom
# listom narudžbi u JSON formatu i prikladnim statusnim kodom.
# Listu narudžbi definirajte globalno, kao praznu listu.
# Vaš konačni poslužitelj mora sadržavati 3 rute: /proizvodi , /proizvodi/{id} i /narudzbe .
# Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.

import asyncio
import aiohttp
from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def proizvod_id_handler(request):
    id_proizvoda = int(request.match_info['id'])
    proizvod = next((p for p in proizvodi if p['id'] == id_proizvoda), None)
    
    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
    return web.json_response(proizvod)

async def narudzbe_handler(request):
    nova_narudzba = await request.json()
    proizvod_id = nova_narudzba['proizvod_id']
    
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    
    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
    nova_narudzba['proizvod_naziv'] = proizvod['naziv']
    nova_narudzba['cijena'] = proizvod['cijena']
    narudzbe.append(nova_narudzba)
    
    return web.json_response(narudzbe, status=201)
    
app = web.Application()

app.router.add_get('/proizvodi', proizvodi_handler)
app.router.add_get('/proizvodi/{id}', proizvod_id_handler)
app.router.add_post('/narudzbe', narudzbe_handler)

async def main():
    async with aiohttp.ClientSession() as session:
        print("GET /proizvodi")
        response = await session.get("http://localhost:8081/proizvodi")
        proizvodi_data = await response.json()
        print(proizvodi_data)
        
        print("\nGET /proizvodi/4")
        response = await session.get("http://localhost:8081/proizvodi/4")
        proizvod_data = await response.json()
        print(proizvod_data)
        
        print("\nPOST /narudzbe")
        narudzba_data = {"proizvod_id": 1, "kolicina": 2}
        response = await session.post("http://localhost:8081/narudzbe", json=narudzba_data)
        narudzbe_data = await response.json()
        print(narudzbe_data)
        
        print("\nPOST /narudzbe")
        narudzba_data = {"proizvod_id": 69, "kolicina": 1}
        response = await session.post("http://localhost:8081/narudzbe", json=narudzba_data)
        error_data = await response.json()
        print(error_data)

web.run_app(app, host="localhost", port=8081)
asyncio.run(main())
