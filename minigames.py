import random
import requests

API_BASE_URL = "https://pokeapi.co/api/v2/"
POKEMON_COUNT = 649

def get_random_pokemon_id():
    return random.randint(1, POKEMON_COUNT)

def get_pokemon_info(pokemon_id):
    url = API_BASE_URL + f"pokemon/{pokemon_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_random_pokemon_options(correct_pokemon):
    options = [correct_pokemon["name"]]
    while len(options) < 4:
        pokemon_id = get_random_pokemon_id()
        pokemon_info = get_pokemon_info(pokemon_id)
        if pokemon_info and pokemon_info["name"] not in options:
            options.append(pokemon_info["name"])
    random.shuffle(options)
    return options

def play_game():
    print("Minijuegos con Python")
    while True:
        print("\n1. Adivina el Pokémon")
        print("0. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            pokemon_id = get_random_pokemon_id()
            pokemon_info = get_pokemon_info(pokemon_id)

            if pokemon_info:
                print("\nWho's That Pokémon?")
                print("Pista:", end=" ")
                abilities = [ability["ability"]["name"] for ability in pokemon_info["abilities"]]
                types = [type_entry["type"]["name"] for type_entry in pokemon_info["types"]]
                print("/".join(types))

                options = get_random_pokemon_options(pokemon_info)
                for i, option in enumerate(options):
                    print(f"{i+1}. {option.capitalize()}")

                while True:
                    user_choice = input("\nIngresa el número de tu elección: ")
                    if user_choice.isdigit() and 1 <= int(user_choice) <= 4:
                        break
                    print("Por favor, ingresa un número válido del 1 al 4.")

                if options[int(user_choice) - 1] == pokemon_info["name"]:
                    print("¡Correcto! ¡Eres un maestro Pokémon!")
                else:
                    print("Incorrecto. ¡Sigue intentándolo!")

            else:
                print("No se pudo obtener la información del Pokémon. Inténtalo nuevamente.")

        elif choice == "0":
            print("Gracias por jugar. ¡Hasta luego!")
            break

        else:
            print("Por favor, ingresa una opción válida (0 o 1).")

play_game()
