user_name = input("Ingrese su nombre de usuario: ")
user_last_name = input("Ingrese su apellido de usuario: ")
user_age = int(input("Ingrese su edad: "))

match user_age:
    case age if age < 2:
        print(f"Estimado {user_name} {user_last_name}, Eres un bebe")
    case age if age >= 2 and age < 10:
        print(f"Estimado {user_name} {user_last_name}, Eres un niño")
    case age if age >= 10 and age < 12:
        print(f"Estimado {user_name} {user_last_name}, Eres un preadolescente")
    case age if age >= 12 and age < 18:
        print(f"Estimado {user_name} {user_last_name}, Eres un adolescente")
    case age if age >= 18 and age < 26:
        print(f"Estimado {user_name} {user_last_name}, Eres un adulto joven")
    case age if age >= 26 and age < 65:
        print(f"Estimado {user_name} {user_last_name}, Eres un adulto")
    case age if age >= 65:
        print(f"Estimado {user_name} {user_last_name}, Eres un adulto mayor")
