import json
# Leer archivos JSON

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

# Escribir archivos JSON
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Crear un archivo JSON y escribir en él
with open('data.json', 'w', encoding='utf-8') as file:
  json.dump(x, file, indent=4)

print(json.dumps(x))