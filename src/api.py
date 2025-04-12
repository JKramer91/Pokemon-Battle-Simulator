import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return
    data = response.json()
    return data

def extract_attributes(data):
    attributes = {}
    attributes["name"] = data["name"]
    attributes["id"] = data["id"]
    attributes["stats"] = get_stats(data["stats"])
    attributes["moves"] = get_moves(data["moves"])
    return attributes

def get_stats(stats):
    ivs = {}
    for stat in stats:
        name = stat["stat"]["name"]
        if name == "hp" or name == "attack" or name == "defense":
            ivs[f"{name}"] = stat["base_stat"]
    return ivs

def get_moves(moves):
    selected_moves = []
    for move in moves:
        for detail in move["version_group_details"]:
            if detail["move_learn_method"]["name"] == "level-up" and detail["version_group"]["name"] == "red-blue":
                url = move["move"]["url"]
                response = requests.get(url)
                if response.status_code != 200:
                    return
                data = response.json()
                if data["power"] is not None:
                    move_info = {
                        "name": data["name"],
                        "power": data["power"],
                        "accuracy": data["accuracy"] or 100
                    }
                    selected_moves.append(move_info)
    return selected_moves[:4]