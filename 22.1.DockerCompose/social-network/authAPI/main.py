from aiohttp import web
import hashlib

korisnici = [
  {"korisnicko_ime": "admin", "lozinka_hash" : "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"}, # lozinka = "lozinka123"
  {"korisnicko_ime": "markoMaric", "lozinka_hash" : "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"}, # lozinka = "markoKralj123"
  {"korisnicko_ime": "ivanHorvat", "lozinka_hash" : "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"}, # lozinka = "lllllllllllozinka_123"
  {"korisnicko_ime": "Nada000", "lozinka_hash":"492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"} # lozinka = "blablabla"
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def add_user(request):
    request_data = await request.json()
    korisnicko_ime = request_data["korisnicko_ime"]
    lozinka = request_data["lozinka"]
    
    if any(korisnik["korisnicko_ime"] == korisnicko_ime for korisnik in korisnici):
        return web.json_response({"error": "Korisnik s ovim korisnickim imenom vec postoji"}, status=400)
    
    lozinka_hash = hash_data(lozinka)

    korisnici.append({"korisnicko_ime": korisnicko_ime, "lozinka_hash": lozinka_hash})
    return web.json_response({"message": "Korisnik je uspjesno stvoren"}, status=200)

async def login(request):
    request_data = await request.json()
    korisnicko_ime = request_data["korisnicko_ime"]

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime: 
            lozinka = request_data["lozinka"]
            lozinka_hash = hash_data(lozinka)

            if korisnik["lozinka_hash"] == lozinka_hash:
                return web.json_response({"autoriziran": True}, status=200)

            return web.json_response({"autoriziran": False}, status=401)
        

    return web.json_response({"error": "Korisnik s ovim korisnickim imenom ne postoji"}, status=404)

app = web.Application()

app.router.add_post("/register", add_user)
app.router.add_post("/login", login)

if __name__ == "__main__":
    web.run_app(app, port=9000)

'''
Definirajte jednostavni aiohttp mikroservis authAPI koji će slušati na portu 9000. 
Mikroservis pohranjuje in-memory podatke o korisnicima, s hashiranim lozinkama. U komentarima 
pored svakog zapisa možete pronaći stvarnu lozinku koja je korištena za generiranje hash vrijednosti funkcijom hash_data.

implementirajte rutu POST /register koja dodaje novog korisnika u listu korisnika. Pohranite samo hashiranu lozinku korisnika.

implementirajte rutu POST /login koja pronalazi korisnika po korisničkom imenu u listi korisnika i provjerava je li unesena lozinka u tijelu HTTP zahtjeva ispravna, odnosno podudaraju li se hash vrijednosti. Ako se pokuša prijaviti korisnik koji ne postoji, vratite odgovarajući statusni kod i poruku. Ako se lozinke ne podudaraju, vratite odgovarajući statusni kod i poruku.

definirajte Dockerfile za authAPI mikroservis i pokrenite ga u Docker kontejneru. Servis treba slušati na portu 9000 domaćina.
'''
