from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

automobili = [
    {
        "id": 1,
        "marka": "VW",
        "model": "Polo",
        "godina_proizvodnje": 2007,
        "boja": "Metalic",
        "cijena": 13000
    },
    {
        "id": 2,
        "marka": "Mercedes",
        "model": "Nes",
        "godina_proizvodnje": 2019,
        "boja": "Crvena",
        "cijena": 20101
    }
]

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class SendAutomobil(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str


'''
1. Definirajte rutu i odgovarajući Pydantic model za dohvaćanje podataka o automobilima. 
Svaki automobil ima sljedeće atribute: id, marka, model, godina_proizvodnje, cijena i boja. 
Ako korisnik pokuša dohvatiti automobil s ID-em koji ne postoji, podignite iznimku HTTPException s statusom 404 i porukom Automobil nije pronađen.
'''
@app.get("/automobil/{id}", response_model=Automobil)
def get_automobil_by_id(id: int, max_cijena: float, max_godina: int, min_cijena: float = Query(ge=0), min_godina: int = Query(ge = 1960)):
    if min_cijena > max_cijena or min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Min godina ne smije biti veca od max god te isto vrijedi za cijenu.")

    for automobil in automobili:
        if automobil["id"] == id:
            return automobil
    raise HTTPException(status_code=404, detail=f"Automobil s id-em {id} nije pronaden.")
    

'''
2. Nadogradite prethodnu rutu s query parametrima min_cijena, max_cijena, min_godina i max_godina. 
Implementirajte validaciju query parametra za cijenu i godinu proizvodnje. Minimalna cijena mora biti veća od 0, 
a minimalna godina proizvodnje mora biti veća od 1960. Unutar funkcije obradite iznimku kada korisnik unese 
minimalnu cijenu veću od maksimalne cijene ili minimalnu godinu proizvodnje veću od maksimalne godine proizvodnje te vratite odgovarajući HTTPException.
'''
# Rijeseno je u prethodnom zad.

'''
3. Definirajte rutu za dodavanje novog automobila u bazu podataka. id se mora dodati na poslužitelju, 
kao i atribut cijena_pdv (definirajte dodatni Pydantic model za to). Ako korisnik pokuša dodati automobil 
koji već postoji u bazi podataka, podignite odgovarajuću iznimku. Implementirajte ukupno 3 Pydantic modela, 
uključujući BaseCar model koji će nasljeđivati preostala 2 modela.
'''
# cijena_pdv nisam implementirao zato jer kada cemo GET-at model ce javiti gresku jer je jedan atribut vise gledajuci response_model. 
# Kao sto je u 1. zad receno "Svaki automobil ima sljedeće atribute: id, marka, model, godina_proizvodnje, cijena i boja." 

@app.post("/automobil/", response_model=Automobil)
def post_automobil(automobil: SendAutomobil):
    for auto in automobili:
        if (auto["marka"] == automobil.marka and auto["model"] == automobil.model and auto["godina_proizvodnje"] == automobil.godina_proizvodnje 
            and auto["cijena"] == automobil.cijena and auto["boja"] == automobil.boja):
                raise HTTPException(status_code=400, detail="Automobil vec postoji.")

    new_id = len(automobili) + 1
    automobil_s_id = Automobil(id=new_id, **automobil.model_dump())
    automobili.append(automobil_s_id.model_dump())
    return automobil_s_id

