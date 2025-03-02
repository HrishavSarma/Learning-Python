# How to connect to an API using python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) # gives response codes
    print(response) # list of response codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

    if response.status_code == 200:
        print("Data retrieved successfully")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "mightyena"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    try:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Weight: {pokemon_info['weight']}")
        print(f"Height: {pokemon_info['height']}")
    except KeyError as e:
        print(f"Wrong Key input: {e.args[0]}")