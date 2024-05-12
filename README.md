# POKEDEX_Diego_Cervantes_Proyecto_M4
En este proyecto, se generó un código donde se da a conocer las librerias request, json, donde permite hacer peticiones en HTTP, donde podemos encontrar las generalidades de su funcionamiento, como conocer las características de los pokemones que se encuentran dentro de la PokeAPI.


import os
import requests                                                               Se ingresan las librerias con las que estara dando el funcionamiento al codigó
import json

def obtener_datos_pokemon(nombre):                                            Se ingresan y definen las variables para poder dar a conocer las caracteristicas de los pokemones que estan dentro de PokeAPI
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

def guardar_en_json(datos, nombre):                               Se ingresa libreria la cual nos permitira guardar las caracteristicas del pokemon dentro de una carpeta y el URL de la imagen del pokemon
    if not os.path.exists('pokedex'):                             dentro de la libreria json.
        os.makedirs('pokedex')
    with open(f"pokedex/{nombre.lower()}.json", "w") as file:
        json.dump(datos, file)

def main():                                                        Aqui es donde el usuario debera ingresar el nombre del pokemon a elegir y le estara mostrandando la caracteristicas del mismo y a su vez
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")    lo estara guardando dentro de una carpeta "pokedex".json
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
        print("¡Error! Pokémon no encontrado.")                    Si el usuario ingresa de un pokemon que no estan dentro del PokeAPI enseguida le arrojara el mensaje de "Error, Pokemon no encontrado"

if __name__ == "__main__":
    main()

                                                           Este codigo me ha enseñado la funcionalida que hay con otras librerias, sus funcionamientos, el saber interactuar con APIsweb, el como se procesan 
                                                           datos .json en archivos Python para el almacenamiento de datos, asi como aprender a manejar errores y estructurar un proyecto.
