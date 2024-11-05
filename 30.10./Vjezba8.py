def filtriraj_parne(lista):
    evenList = [x for x in lista if x % 2 == 0]
    return evenList

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista)) # [2, 4, 6, 8, 10]
