from api import get_pokemon_data, extract_attributes
from pokemon import Pokemon
from healthbar import HealthBar

class Game:
    def __init__(self):
        self.player_pokemon = None
        self.enemy_pokemon = None
        self.player_healthbar = None
        self.enemy_healthbare = None
        self.is_initialized = False

    def setup(self, pokemon):
        player_data = get_pokemon_data(pokemon)
        attributes = extract_attributes(player_data)
        enemy_data = get_pokemon_data("charmander")
        enemy_attributes = extract_attributes(enemy_data)
        self.player_pokemon = Pokemon(attributes)
        self.enemy_pokemon = Pokemon(enemy_attributes)
        self.player_healthbar = HealthBar(125, 420, 200, 20, self.player_pokemon.current_hp)
        self.enemy_healthbar = HealthBar(755, 245, 200, 20, self.player_pokemon.current_hp)

        # Signals that the game is properly setup and that playing can start
        self.is_initialized = True

        
