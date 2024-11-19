#1. kvadriranje broja
kvadriraj = lambda x: x ** 2
print(kvadriraj(3), kvadriraj(-2), kvadriraj(0))

#2. zbroji pa kvadriraj 
zbroji_pa_kvadriaj = lambda a, b: (a + b) ** 2
print(zbroji_pa_kvadriaj(2, 3), zbroji_pa_kvadriaj(4, -4))

#3. kvadriraj duljinu niza
kvadriraj_duljinu = lambda niz: len(niz) ** 2
print(kvadriraj_duljinu("nesto"), kvadriraj_duljinu("tamo"))

#4. pomnozi vrijednost s 5 pa potenciraj na x
pomnozi_i_potenciraj = lambda x, y: (y * 5) ** x
print(pomnozi_i_potenciraj(1, 2), pomnozi_i_potenciraj(2, 0))

#5. vrati True ako je broj paran, inače vrati None
paran_broj = lambda x: True if x % 2 == 0 else None
print(paran_broj(4), paran_broj(3), paran_broj(0))
