from api import get_pokemon_data, extract_attributes
from pokemon import Pokemon
from healthbar import HealthBar
from enum import Enum, auto

class GameState(Enum):
    PLAYER_TURN = auto()
    ENEMY_TURN = auto()
    WON = auto()
    LOST = auto()

class Game:
    def __init__(self):
        self.player_pokemon = None
        self.enemy_pokemon = None
        self.player_healthbar = None
        self.enemy_healthbare = None
        self.game_state = None
        self.is_initialized = False
        self.is_game_over = False

    def setup(self, pokemon):
        player_data = get_pokemon_data(pokemon)
        attributes = extract_attributes(player_data)
        enemy_data = get_pokemon_data("charmander")
        enemy_attributes = extract_attributes(enemy_data)
        self.player_pokemon = Pokemon(attributes)
        self.enemy_pokemon = Pokemon(enemy_attributes)
        self.player_healthbar = HealthBar(125, 420, 200, 20, self.player_pokemon.current_hp)
        self.enemy_healthbar = HealthBar(755, 245, 200, 20, self.player_pokemon.current_hp)
        self.game_state = GameState.PLAYER_TURN

        # Signals that the game is properly setup and that playing can start
        self.is_initialized = True

    def game_on(self, ui_manager):
       #while not self.is_game_over:
        self.handle_states(self.game_state, ui_manager)

    def handle_states(self, game_state, ui_manager):
        match game_state:
            case GameState.PLAYER_TURN:
                self.handle_player_turn(ui_manager)
            case GameState.ENEMY_TURN:
                self.handle_enemy_turn()
            case GameState.WON:
                print("You won!")
                self.is_game_over = True
            case GameState.LOST:
                print("You lost")
                self.is_game_over = True

    def handle_player_turn(self, ui_manager):
        #print("Players turn!")
        if ui_manager.game_buttons[1].check_click():
            self.player_attack(self.player_pokemon.moves[0])
    
    def player_attack(self, move):
        #print("move: " + str(move["power"]))
        #print("hp: " + str(self.enemy_pokemon.current_hp))
        self.enemy_pokemon.current_hp -= 1
        if self.enemy_pokemon.current_hp <= 0:
            self.game_state = GameState.WON
        else:
            self.game_state = GameState.ENEMY_TURN
    
    def handle_enemy_turn(self):
        #print("Enemys turn!")
        #self.player_pokemon.current_hp -= 1

        if self.player_pokemon.current_hp <= 0:
            self.game_state = GameState.LOST
        else:
            self.game_state = GameState.PLAYER_TURN