print("=== Mi Primera Calculadora ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")

if num2 != 0:
    division = num1 / num2
    print(f"La división es: {division}")
else:
    print("La división no es posible entre cero.")
