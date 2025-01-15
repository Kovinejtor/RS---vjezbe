from fastapi import FastAPI
from typing import List
from models import Film, CreateFilm

app = FastAPI()

filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

# 1. Definirajte novu FastAPI rutu GET /filmovi koja će klijentu vraćati listu filmova definiranu u sljedećoj listi

@app.get("/filmovi/", response_model=List[Film])
async def get_all_filmovi(genre: str | None = None, min_godina: int = 2000):
    chosen_filmovi = [film for film in filmovi if (film["genre"] == genre or genre is None) and film["godina"] >= min_godina]
    return chosen_filmovi


# 2. Nadogradite prethodnu rutu na način da će output biti validiran Pydantic modelom Film kojeg definirate u zasebnoj datoteci models.py.
# Rijeseno je pod prethodnim.


'''
3. Definirajte novu FastAPI rutu GET /filmovi/{id} koja će omogućiti pretraživanje novog filma 
prema id-u definiranom u parametru rute id. Dodajte i ovdje validaciju Pydantic modelom Film.
'''
@app.get("/filmovi/{id}", response_model=Film)
async def get_film_by_id(id: int):
    specific_film = next((film for film in filmovi if film["id"] == id), None)
    return specific_film


'''
4. Definirajte novu rutu POST /filmovi koja će omogućiti dodavanje novog filma u listu filmova. 
Napravite novi Pydantic model CreateFilm koji će sadržavati atribute naziv, genre i godina, 
a kao output vraćajte validirani Pydantic model Film koji predstavlja novododani film s automatski dodijeljenim id-em.
'''
@app.post("/filmovi/", response_model=Film)
async def post_film(film: CreateFilm):
    if filmovi:
        next_id = max(film["id"] for film in filmovi) + 1
    else:
        next_id = 1
    
    new_film = Film(id=next_id, **film.dict())
    filmovi.append(new_film.dict())

    return new_film


'''
5. Dodajte query parametre u rutu GET /filmovi koji će omogućiti filtriranje filmova 
prema genre i min_godina. Zadane vrijednosti za query parametre neka budu None i 2000.
'''
# Rijeseno je pod 1. zad.

