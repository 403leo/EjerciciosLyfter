import json


# Logica para ingresar un nuervo pokemosn al JSON.

def enter_new_pokemon():
    name = input("Ingrese el nombre del Pokémon: ")
    type_ = input("Ingrese el tipo del Pokémon: ")
    level = int(input("Ingrese el nivel del Pokémon: "))
    weight_kg = float(input("Ingrese el peso en kg del Pokémon: "))
    is_shiny = input("¿Es brillante? (true/false): ").lower() == "true"
    held_item = input("Ingrese el objeto que sostiene (o deje en blanco si no tiene): ")
    held_item = held_item if held_item else None
    skills = input("Ingrese las habilidades separadas por comas: ").split(",")
    skills = [skill.strip() for skill in skills]
    
    stats = {
        "hp": int(input("Ingrese los puntos de vida (HP): ")),
        "attack": int(input("Ingrese el ataque: ")),
        "defense": int(input("Ingrese la defensa: ")),
        "sp_attack": int(input("Ingrese el ataque especial: ")),
        "sp_defense": int(input("Ingrese la defensa especial: ")),
        "speed": int(input("Ingrese la velocidad: "))
    }
    
    new_pokemon = {
        "name": name,
        "type": type_,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }
    
    return new_pokemon


# load existing pokemon from the JSON file
def load_pokemons_from_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save pokemon to the JSON file
def save_pokemons_to_json(pokemons, file_path):
      with open(file_path, "w") as f:
         json.dump(pokemons, f, indent=4)


def main():

    # Load existing pokemons from the JSON file
    existing_pokemons = load_pokemons_from_json("pokemons.json")

    # Enter a new Pokémon
    new_pokemon = enter_new_pokemon()

    # Add the new Pokémon to the existing list
    existing_pokemons.append(new_pokemon)

    # Save the updated list of Pokémon to the JSON file
    save_pokemons_to_json(existing_pokemons, "pokemons.json")

    # print the updated list of Pokémon
    print("Lista actualizada de Pokémon:")
    print(json.dumps(existing_pokemons, indent=4))

main()