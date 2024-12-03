# Zadatak 2: POST /proizvodi
# Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve
# s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv , cijena i količina .
# Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti
# odgovor s novom listom proizvoda u JSON formatu.

from aiohttp import web

app = web.Application()

proizvodi = [
    {"naziv": "Torba", "cijena": 12, "kolicina": 2},
    {"naziv": "Nes", "cijena": 14, "kolicina": 3}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi)

async def post_proizvodi(request):
    novi_proizvod = await request.json()
    print("Dobiveni proizvod:", novi_proizvod) 

    proizvodi.append(novi_proizvod)
    return web.json_response(proizvodi)

app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_post("/proizvodi", post_proizvodi)

web.run_app(app, host="localhost", port=8081)
