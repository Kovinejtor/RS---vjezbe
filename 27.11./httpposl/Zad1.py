# Zadatak 1: GET /proizvodi
# Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
# JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
# adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
from aiohttp import web

app = web.Application()

proizvodi = [
    {"naziv": "Torba", "cijena": 12, "kolicina": 2},
    {"naziv": "Nes", "cijena": 14, "kolicina": 3}
]

async def proizvodi_function(request):
    return web.json_response(proizvodi)

app.router.add_get("/proizvodi", proizvodi_function)

web.run_app(app, host = "localhost", port = 8081) 
