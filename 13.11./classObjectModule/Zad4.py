from datetime import datetime
import math
pi = math.pi

'''
1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
Dodajte metodu ispis koja će ispisivati sve atribute automobila.
Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
godine dohvatite pomoću datetime modula.
'''
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka 
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        return f"Marka: {self.marka}, model: {self.model}, godina_proizvodnje: {self.godina_proizvodnje}, kilometraza: {self.kilometraza}"

    def starost(self):
        return f"Starost vozila u godinama: {datetime.now().year - self.godina_proizvodnje}"

automobil = Automobil("VW", "Polo 5", 2019, 20000)
print(automobil.ispis())
print(automobil.starost())

'''
2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
b .
'''
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b 

    def dijeljenje(self):
        return self.a / self.b 

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return self.a ** (1 / self.b)

'''
3. Definirajte klasu Student s atributima ime , prezime , godine i ocjene .
Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
novu listu studenti_objekti :
Dodajte metodu prosjek koja će računati prosječnu ocjenu studenta.
U varijablu najbolji_student pohranite studenta s najvećim prosjekom ocjena iz liste
studenti_objekti . Implementirajte u jednoj liniji koda.
'''

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
    
    def __repr__(self):
        return f"Student(ime={self.ime}, prezime={self.prezime}, godine={self.godine}, ocjene={self.ocjene})"

studenti_objekti = [Student(i["ime"], i["prezime"], i["godine"], i["ocjene"]) for i in studenti]
print(studenti_objekti)

najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())
print(najbolji_student)

'''
4. Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
površinu kruga.
Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.
'''
class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * self.r * pi

    def povrsina(self):
        return self.r ** 2 * pi

krug = Krug(3)
print(krug.opseg())
print(krug.povrsina())

'''
5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
"Radim na poziciji {pozicija}".
Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
povećava plaću radnika ( Radnik ) za iznos povecanje .
Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
give_raise .
'''

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        return f"Radim na poziciji {self.pozicija}"

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        return f"Nova placa: {radnik.placa}"

radnik = Radnik("Jozo", "Taksist", 1069)
manager = Manager("Bozo", "Manager", 1420, "Manager nepalskih taksista")

print(radnik.work())
print(manager.work())

print(manager.give_raise(radnik, 0.1))

