import os

# Un único color turquesa/ciano brillante
COLOR = "\033[1;36m"
RESET = "\033[0m"

def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "Error: División por cero"

while True:
    print(f"\n{COLOR}┌────────────────────────────────────────┐")
    print(f"│        🧮 CALCULADORA DE SARAY         │")
    print(f"├────────────────────────────────────────┤")
    print(f"│  1. Sumar (+)                          │")
    print(f"│  2. Restar (-)                         │")
    print(f"│  3. Multiplicar (×)                    │")
    print(f"│  4. Dividir (÷)                        │")
    print(f"│  5. Salir                              │")
    print(f"└────────────────────────────────────────┘{RESET}")

    opcion = input(f"\n{COLOR}Elige una opción (1-5): {RESET}")

    if opcion == "5":
        print(f"\n{COLOR}¡Hasta luego, Saray! ✨{RESET}\n")
        break

    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input(f"{COLOR}Ingresa el primer número: {RESET}"))
            num2 = float(input(f"{COLOR}Ingresa el segundo número: {RESET}"))

            if opcion == "1": res, op = sumar(num1, num2), "+"
            elif opcion == "2": res, op = restar(num1, num2), "-"
            elif opcion == "3": res, op = multiplicar(num1, num2), "×"
            elif opcion == "4": res, op = dividir(num1, num2), "÷"

            print(f"\n{COLOR}▶ Resultado: {num1} {op} {num2} = {res}{RESET}")
        except ValueError:
            print(f"\n{COLOR}⚠️ Por favor ingresa un número válido.{RESET}")
    else:
        print(f"\n{COLOR}⚠️ Opción no válida.{RESET}")
