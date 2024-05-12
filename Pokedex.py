import os
import requests
import json

def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        imagen_url = data['sprites']['front_default']
        peso = data['weight']
        altura = data['height']
        movimientos = [move['move']['name'] for move in data['moves']]
        habilidades = [ability['ability']['name'] for ability in data['abilities']]
        tipos = [tipo['type']['name'] for tipo in data['types']]
        return {
            'imagen': imagen_url,
            'peso': peso,
            'altura': altura,
            'movimientos': movimientos,
            'habilidades': habilidades,
            'tipos': tipos
        }
    else:
        return None

def guardar_en_json(datos, nombre):
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')
    with open(f"pokedex/{nombre.lower()}.json", "w") as file:
        json.dump(datos, file)

def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    datos_pokemon = obtener_datos_pokemon(nombre_pokemon)
    if datos_pokemon:
        print(f"Imagen: {datos_pokemon['imagen']}")
        print(f"Peso: {datos_pokemon['peso']}")
        print(f"Altura: {datos_pokemon['altura']}")
        print(f"Movimientos: {', '.join(datos_pokemon['movimientos'])}")
        print(f"Habilidades: {', '.join(datos_pokemon['habilidades'])}")
        print(f"Tipos: {', '.join(datos_pokemon['tipos'])}")
        guardar_en_json(datos_pokemon, nombre_pokemon)
    else:
        print("¡Error! Pokémon no encontrado.")

if __name__ == "__main__":
    main()