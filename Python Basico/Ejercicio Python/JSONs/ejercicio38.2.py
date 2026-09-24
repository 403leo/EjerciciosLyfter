import json

pokemons = [

   {
      "name":"Pikachu",
      "type":"Electric",
      "level":54,
      "weight_kg":6.0,
      "is_shiny":False,
      "held_item":None,
      "skills":[
         "Thunder Shock",
         "Quick Attack",
         "Thunderbolt",
         "Volt Tackle"
      ],
      "stats":{
         "hp":35,
         "attack":55,
         "defense":40,
         "sp_attack":50,
         "sp_defense":50,
         "speed":90
      }
   },
   
   {
      "name":"Charmander",
      "type":"Fire",
      "level":8,
      "weight_kg":8.5,
      "is_shiny":True,
      "held_item":"Charcoal",
      "skills":[
         "Ember",
         "Scratch",
         "Tackle",
         "Smokescreen"
      ],
      "stats":{
         "hp":39,
         "attack":52,
         "defense":43,
         "sp_attack":60,
         "sp_defense":50,
         "speed":65
      }
   }
]

# Pasar lista a un archivo JSON llamada pokemons.json
with open("pokemons.json", "w") as f:
    json.dump(pokemons, f)


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

# Leer el archivo JSON existente
with open("pokemons.json", "r") as f:
    existing_pokemons = json.load(f)

# Agregar el nuevo Pokémon a la lista existente
new_pokemon = enter_new_pokemon()
existing_pokemons.append(new_pokemon)

# Escribir la lista actualizada de Pokémon en el archivo JSON
with open("pokemons.json", "w") as f:
    json.dump(existing_pokemons, f)

# Imprimir la lista actualizada de Pokémon
print("Lista actualizada de Pokémon:")
print(json.dumps(existing_pokemons))
