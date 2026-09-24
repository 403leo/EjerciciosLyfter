try:

    username = input("Ingrese su nombre: ")

    if username.isdigit():
        raise ValueError("El nombre no puede ser un número.")

    try:
        age = int(input("Ingrese su edad: "))
    except ValueError:
        raise ValueError("La edad debe ser un número.")

    print(f"Hola {username}, su edad es {age} años.")


except ValueError as e:
    print(f"Error: {e}")

