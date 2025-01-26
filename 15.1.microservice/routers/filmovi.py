from fastapi import APIRouter, HTTPException, Query
import json
from models.models import Film
import os
from datetime import datetime
import re
from typing import Optional, Literal

router = APIRouter()

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Film.JSON")

def preprocess_film_data(film: dict) -> dict:
    key_mapping = {       # alias direktno u pydantic model nije radilo
        "Title": "title",
        "Year": "year",
        "Rated": "rated",
        "Released": "released",
        "Runtime": "runtime",
        "Genre": "genre",
        "Director": "director",
        "Writer": "writer",
        "Actors": "actors",
        "Plot": "plot",
        "Language": "language",
        "Country": "country",
        "Awards": "awards",
        "Poster": "poster",
        "Metascore": "metascore",
        "imdbRating": "imdbRating",
        "imdbVotes": "imdbVotes",
        "imdbID": "imdbID",
        "Type": "type",
        "Response": "response",
        "Images": "images",
    }

    transformed_film = {key_mapping.get(k, k): v for k, v in film.items()}

    if "Year" in film:
        match = re.search(r"\d{4}", film["Year"])  # random BS kojeg se ne bi sjetio
        transformed_film["year"] = int(match.group()) if match else None
    else:
        transformed_film["year"] = None

    if "Released" in film and film["Released"] not in ("", "N/A"):
        try:
            transformed_film["released"] = datetime.strptime(film["Released"], "%d %b %Y")
        except ValueError:
            transformed_film["released"] = None
    else:
        transformed_film["released"] = None

    if "imdbRating" in film and film["imdbRating"] not in ("", "N/A"):
        try:
            transformed_film["imdbRating"] = float(film["imdbRating"])
        except ValueError:
            transformed_film["imdbRating"] = None
    else:
        transformed_film["imdbRating"] = None

    if "imdbVotes" in film and film["imdbVotes"] not in ("", "N/A"):
        try:
            transformed_film["imdbVotes"] = int(film["imdbVotes"].replace(",", ""))
        except ValueError:
            transformed_film["imdbVotes"] = None
    else:
        transformed_film["imdbVotes"] = None

    if "Metascore" in film and film["Metascore"].isdigit():
        transformed_film["metascore"] = int(film["Metascore"])
    else:
        transformed_film["metascore"] = None

    transformed_film["genre"] = [genre.strip() for genre in film["Genre"].split(",")] if "Genre" in film else []
    transformed_film["language"] = [lang.strip() for lang in film["Language"].split(",")] if "Language" in film else []
    transformed_film["country"] = [country.strip() for country in film["Country"].split(",")] if "Country" in film else []
    transformed_film["actors"] = [actor.strip() for actor in film["Actors"].split(",")] if "Actors" in film else []

    transformed_film["response"] = film["Response"].lower() == "true" if "Response" in film else None

    transformed_film["images"] = film["Images"] if "Images" in film else None

    return transformed_film


with open(file_path, "r") as f:
    films_data = json.load(f)

films = [Film(**preprocess_film_data(film)) for film in films_data]


@router.get("/films")
async def get_films(
    min_year: Optional[int] = Query(None, ge=1900),
    max_year: Optional[int] = Query(None, le=datetime.now().year),
    min_rating: Optional[float] = Query(None),
    max_rating: Optional[float] = Query(None),
    type: Optional[Literal["movie", "series"]] = Query(None, regex="^(movie|series)$") # isto random BS s reg al nije radilo iz prve
):
    filtered_films = films

    if min_year is not None:
        filtered_films = [film for film in filtered_films if film.year >= min_year]

    if max_year is not None:
        filtered_films = [film for film in filtered_films if film.year <= max_year]

    if min_rating is not None:
        if min_rating < 0 or min_rating > 10:
            raise ValueError("min_rating must be between 0 and 10")
        filtered_films = [film for film in filtered_films if film.imdbRating is not None and film.imdbRating >= min_rating]

    if max_rating is not None:
        if max_rating < 0 or max_rating > 10:
            raise ValueError("max_rating must be between 0 and 10")
        filtered_films = [film for film in filtered_films if film.imdbRating is not None and film.imdbRating <= max_rating]

    if type is not None:
        filtered_films = [film for film in filtered_films if film.type == type]

    return filtered_films

@router.get("/film/{imdb_id}")
async def get_film_by_imdb_id(imdb_id: str):
    film = next((film for film in films if film.imdbID == imdb_id), None)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@router.get("/film/title/{title}")
async def get_film_by_title(title: str):
    film = next((film for film in films if film.title.lower() == title.lower()), None)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film


'''
Strukturirajte kod u zasebnim datotekma unutar direktorija routers i models. 
U direktoriju routers dodajte datoteku filmovi.py u kojoj ćete definirati rute 
za dohvaćanje svih filmova i pojedinog filma po imdbID-u i rutu za dohvaćanje filma prema naslovu (Title).

Za rutu koja dohvaća sve filmove, implementirajte mogućnost filtriranja filmova prema query parametrima: 
min_year, max_year, min_rating, max_rating te type (film ili serija). Implementirajte validaciju query parametra.
U glavnoj aplikaciji učitajte rute iz datoteke filmovi.py i uključite ih u glavnu FastAPI aplikaciju.
Dodajte iznimke (HTTPException) za slučaj kada korisnik pokuša dohvatiti film koji ne postoji u bazi podataka, po imdbID-u ili Title-u.
'''
