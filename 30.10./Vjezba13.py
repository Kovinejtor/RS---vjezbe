def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

def maks_i_min(lista):
    lista.sort()
    return (lista[-1], lista[0]) 

def presjek(skup_1, skup_2):
    return skup_1.intersection(skup_2)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista)) # (1, 10)

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista)) # (250, 5)

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2)) # {4, 5}
