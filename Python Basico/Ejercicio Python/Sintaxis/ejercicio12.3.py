import random

user_number = int(input("Ingrese un número: "))
random_number = random.randint(1, 10)

while user_number != random_number:
    print("¡Incorrecto! Intenta de nuevo.")
    user_number = int(input("Ingrese un número: "))

print("¡Felicidades! Adivinaste el número.")