def ukloni_duplikate(lista):
    setOfList = set(lista)
    return list(setOfList)

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista)) # [1, 2, 3, 4, 5]
