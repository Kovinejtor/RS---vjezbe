# Zadatak 4: Dohvaćanje proizvoda
# Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
# /proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
# prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
# {'error': 'Proizvod s traženim ID-em ne postoji'} .
# Proizvode pohranite u listu rječnika:

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

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def proizvod_id_handler(request):
    id_proizvoda = int(request.match_info['id']) 
    proizvod = next((p for p in proizvodi if p['id'] == id_proizvoda), None)
    
    if proizvod is None:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    
    return web.json_response(proizvod)

app = web.Application()

app.router.add_get('/proizvodi', proizvodi_handler)
app.router.add_get('/proizvodi/{id}', proizvod_id_handler)

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
        
        print("\nGET /proizvodi/69")
        response = await session.get("http://localhost:8081/proizvodi/69")
        error_data = await response.json()
        print(error_data)

web.run_app(app, host="localhost", port=8081)
asyncio.run(main())
