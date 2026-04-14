# Pedir datos al usuario
nombre = input("¿Cómo te llamas? ")
edad_str = input("¿Cuántos años tienes? ")

# Convertir string a int
edad = int(edad_str)

# f-strings → la forma moderna y limpia
print(f"¡Hola {nombre}! Tienes {edad} años.")
print(f"En 5 años tendrás {edad + 5} años. 😎")