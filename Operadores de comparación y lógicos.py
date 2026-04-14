# Comparación
print(5 > 3)     # True
print(10 == 10)  # True
print(7 != 8)    # True
print(4 <= 4)    # True

# Lógicos
es_mayor_de_edad = True
tiene_dinero = False

puede_comprar = es_mayor_de_edad and tiene_dinero  # False
puede_mentir = es_mayor_de_edad or tiene_dinero    # True
no_es_menor = not es_mayor_de_edad                 # False

print(f"Puede comprar alcohol? {puede_comprar}")