from models import *
from fastapi import FastAPI, HTTPException
import aiohttp

app = FastAPI()

posts = [
    {"id": 1, "korisnik": "David", "tekst": "Neka objava", "vrijeme": "2024-12-23T00:00:00"},
    {"id": 2, "korisnik": "Lucija", "tekst": "Hej tamo", "vrijeme": "2023-11-16T00:00:00"}
]

@app.post("/objava", response_model=objava)
async def post_objava(objava: addObjava):
    new_id = len(posts) + 1
    new_post = {"id": new_id, **objava.model_dump()}
    posts.append(new_post)

    return new_post

@app.get("/objava/{id}", response_model=objava)
async def get_objava_by_id(id: int):
    post_with_id = next((post for post in posts if post["id"] == id ), None)

    if post_with_id == None:
        raise HTTPException(status_code=404, detail="Ne postoji objava s ovim id-em")

    return post_with_id

@app.get("/korisnici/{korisnik}/objave")
async def objave_korisnika(korisnik: str, podaci: Podaci):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://authapi:9000/login", json=podaci.model_dump())

        if response.status != 200:
            raise HTTPException(status_code=401, detail="Autorizacija nije uspjela.")
    posts_user = [post for post in posts if post["korisnik"] == korisnik]

    return posts_user
    


'''
implementirajte rutu POST /objava koja dodaje novu objavu u listu objava. Prije dodavanja u listu, obavezno validirajte ulazne podatke. Prilikom dodavanja objave, sve vrijednosti su obavezne, osim id atributa koji se automatski dodjeljuje. Logiku dodjeljivanja jedinstvenog identifikatora možete implementirati sami po želji.

implementirajte rutu GET /objava/{id} koja dohvaća objavu po jedinstvenom identifikatoru.

implementirajte rutu GET /korisnici/{korisnik}/objave koja dohvaća sve objave korisnika s određenim korisničkim imenom.

definirajte Dockerfile za socialAPI mikroservis i pokrenite ga u Docker kontejneru. Servis treba slušati na portu 3500 domaćina.
'''
