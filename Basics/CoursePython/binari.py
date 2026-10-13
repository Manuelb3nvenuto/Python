#Crear una funcion pra el ealgoritmo de busqueda binaria en la lista

def busqueda_binaria(lista, valor):
    primero = 0 
    ultimo = len(lista) - 1 
    encontrado = False

    while primero <= ultimo and not encontrado:
        mitad = (primero + ultimo) // 2

        if lista[mitad] == valor:
            encontrado = True
        else:
            if valor < lista[mitad]:
                ultimo = mitad - 1
            else:
                primero = mitad + 1
    return encontrado

numeros = [2, 3, 5, 7, 11, 13, 17, 19]

llave = 13    
print(busqueda_binaria(numeros,llave))

llave = 2   
print(busqueda_binaria(numeros, llave))