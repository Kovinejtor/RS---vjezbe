# Zadatak 3: GET /punoljetni
# Definirajte poslužitelj koji sluša na portu 8082 i na putanji /punoljetni vraća listu korisnika starijih od 18
# godina. Svaki korisnik je rječnik koji sadrži ključeve ime i godine . Pošaljite zahtjev na adresu
# http://localhost:8082/stariji_korisnici i provjerite odgovor. Novu listu korisnika definirajte koristeći
# funkciju filter ili list comprehension .

from aiohttp import web

korisnici = [
{'ime': 'Ivo', 'godine': 25},
{'ime': 'Ana', 'godine': 17},
{'ime': 'Marko', 'godine': 19},
{'ime': 'Maja', 'godine': 16},
{'ime': 'Iva', 'godine': 22}
]

async def punoljetni_handler(request):
    punoljetni_korisnici = [korisnik for korisnik in korisnici if korisnik['godine'] >= 18]
    return web.json_response(punoljetni_korisnici)

app = web.Application()
app.router.add_get('/punoljetni', punoljetni_handler)

web.run_app(app, host="localhost", port=8082)
