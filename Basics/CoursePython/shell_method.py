#ejercicio: crear una funcion para el algoritmo shell

def shell_sort(lista):
    n = len(lista)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            reduction_search(lista, i, gap)

        gap = gap // 2

def reduction_search(lista, inicio, saldo):
    for i in range (inicio + saldo, len(lista), saldo):
        valor = lista[i]
        posicion = i

        while posicion >= saldo and lista[posicion - saldo] > valor:
            lista[posicion] = lista[posicion - saldo]
            posicion = posicion - saldo
        lista[posicion] = valor

numeros = [7, 2, 11, 3, 1, 13, 5]
print (numeros)

shell_sort(numeros)
print(numeros)