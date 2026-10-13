#EJERCICIO: CREAR UNA FUNCION PARA EL ALGORITMO DE ORDENAMIENTO DE SELECCION

def ordenamiento_selection(lista):
    for n in range(len(lista)- 1, 0 , -1):
        posicion_max = 0

        for l in range(1, n + 1):
            if lista[l] > lista[posicion_max]:
                posicion_max = 1

        temp = lista[n]
        lista[n] = lista[posicion_max]
        lista[posicion_max] = temp
    
numeros = [19, 17, 2, 29, 3, 5 ,11, 7, 13]
print(numeros)

ordenamiento_selection(numeros)
print(numeros)



