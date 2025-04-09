
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))


if num1 == 0 or num2 == 0:
    print("Los números deben ser distintos de 0. Intenta de nuevo.")
else:

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 


    print("\nResultados:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
    print(f"División: {num1} ÷ {num2} = {division:.2f}")  # Se muestra con 2 decimales
