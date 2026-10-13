# Crear una funcion para el algoritmo de busqueda sobre una lista

def busqueda_lineal(lista, valor):
    posicion = 0
    encontrado = False

    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion += 1 

    return encontrado, posicion

numeros = [2,7,3,5,15,31, 29, 17, 19]
llave = 37
print(busqueda_lineal(numeros,llave))