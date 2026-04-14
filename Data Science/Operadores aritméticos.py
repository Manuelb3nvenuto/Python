a = 10
b = 3

suma = a + b          # 13
resta = a - b         # 7
multiplicacion = a * b  # 30
division = a / b      # 3.333... (siempre float)
division_entera = a // b  # 3
residuo = a % b       # 1
potencia = a ** b     # 1000

print(f"{a} + {b} = {suma}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}" + " | Division tipo float")
print(f"{a} % {b} = {residuo}")
print(f"{a} // {b} = {division_entera} (división entera)")