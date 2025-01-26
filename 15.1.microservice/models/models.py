from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field

class Film(BaseModel):
    title: str
    year: int = Field(ge=1900)
    rated: str
    released: Optional[datetime] = datetime(2008, 12, 22)
    runtime: str
    genre: list[str]
    director: Optional[str] = "James Cameron"
    writer: str
    actors: list[str]
    plot: str
    language: list[str]
    country: list[str]
    awards: Optional[str] = "Won 4 Oscars"
    poster: Optional[str] = "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg"
    metascore: Optional[int] = 69
    imdbRating: Optional[float] = Field(ge=0, le=10, default=34.24)
    imdbVotes: Optional[int] = Field(ge=0, default=736828)
    imdbID: Optional[str] = "tt0499549"
    type: Optional[Literal["movie", "series"]] = "movie" 
    response: Optional[bool] = True
    images: Optional[list[str]]

class Actor(BaseModel):
    name: str 
    surname: str

class Writer(BaseModel):
    name: str
    surname: str

'''
Images mora biti lista stringova (javnih poveznica na slike)
type mora biti odabir između "movie" i "series"
Obavezni atributi su: Title, Year, Rated, Runtime, Genre, Language, Country, Actors, Plot, Writer
Ostali atributi su neobavezni, a ako nisu navedeni, postavite im zadanu vrijednost
Dodajte validacije za Year i Runtime atribut (godina mora biti veća od 1900, a trajanje filma mora biti veće od 0)
Dodajte validacije za imdbRating i imdbVotes (ocjena mora biti između 0 i 10, a broj glasova mora biti veći od 0)
'''

'''
[
  {
    "Title": "Avatar",
    "Year": "2009",
    "Rated": "PG-13",
    "Released": "18 Dec 2009",
    "Runtime": "162 min",
    "Genre": "Action, Adventure, Fantasy",
    "Director": "James Cameron",
    "Writer": "James Cameron",
    "Actors": "Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang",
    "Plot": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "Language": "English, Spanish",
    "Country": "USA, UK",
    "Awards": "Won 3 Oscars. Another 80 wins & 121 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
    "Metascore": "83",
    "imdbRating": "7.9",
    "imdbVotes": "890,617",
    "imdbID": "tt0499549",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTYyMzUxNl5BMl5BanBnXkFtZTcwNTg0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM2MDk3MTcyMV5BMl5BanBnXkFtZTcwNjg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2ODQ3NjMyMl5BMl5BanBnXkFtZTcwODg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxOTEwNDcxN15BMl5BanBnXkFtZTcwOTg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMDg1Nzk1MV5BMl5BanBnXkFtZTcwMDk0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    ]
  },
  ...
]
'''
