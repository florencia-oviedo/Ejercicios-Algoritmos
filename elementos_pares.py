
'''
Dada una lista de elementos (array), 
crear una funcion que retorne una nueva lista con solo los elementos que aparecen una cantidad pares de veces.
["A","B","A","C","C","C","C"] // -> ["A","C"]
[1,2,3,1,2] // -> [1,2]
'''

def elementos_pares(elementos):
    dic = {}
    for elem in elementos:
        if elem in dic:
            dic[elem] +=1 
        else:
            dic[elem] = 1
    
    lista_pares = []

    for key in dic:
        if dic[key] % 2 == 0:
            lista_pares.append(key)

    return lista_pares


if __name__ ==  "__main__":

    lista = [1,2,3,1,2]
    lista_nueva = elementos_pares(lista)
    print(lista_nueva)