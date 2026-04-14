# Calculadora de propinas – Mini proyecto Módulo 1

print("¡Bienvenido a la calculadora de propinas! 💸")

cuenta = float(input("¿Cuánto salió la cuenta total? $"))
porcentaje = float(input("¿Qué % de propina quieres dejar? (10, 15, 20...) "))

propina = cuenta * (porcentaje / 100)
total = cuenta + propina

print(f"\n--- Resultado ---")
print(f"Cuenta: ${cuenta:.2f}")
print(f"Propina ({porcentaje}%): ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")
print("¡Gracias por dejar buena propina! 🍕")