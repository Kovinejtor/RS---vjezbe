def grupiraj_po_paritetu(lista):
    evenList = [x for x in lista if x % 2 == 0]
    oddList = [x for x in lista if x % 2 != 0]
    
    return {'parni': evenList, 'neparni': oddList}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))
# {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}
