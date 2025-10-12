import random, pygame
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
        self.enemy_healthbar = None
        self.game_state = None
        self.is_initialized = False
        self.is_game_over = False
        self.prev_clicked = False
        self.last_attack_time = 0
        self.wait_time = 2000

    def setup(self, pokemon):
        player_data = get_pokemon_data(pokemon)
        attributes = extract_attributes(player_data)
        enemy_data = get_pokemon_data("charmander")
        enemy_attributes = extract_attributes(enemy_data)
        self.player_pokemon = Pokemon(attributes)
        self.enemy_pokemon = Pokemon(enemy_attributes)
        self.player_healthbar = HealthBar(135, 450, 200, 20, self.player_pokemon.current_hp)
        self.enemy_healthbar = HealthBar(810, 350, 200, 20, self.enemy_pokemon.current_hp)
        self.game_state = GameState.PLAYER_TURN

        # Signals that the game is properly setup and that playing can start
        self.is_initialized = True

    def game_on(self, ui_manager):
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
        is_move_clicked, idx = ui_manager.is_move_clicked()
        if is_move_clicked and not self.prev_clicked:
            self.prev_clicked = True
            self.player_attack(self.player_pokemon.moves[idx])
        
        if not is_move_clicked:
            self.prev_clicked = False

    def player_attack(self, move):
        print(f"{self.player_pokemon.name} attacked {self.enemy_pokemon.name}")
        self.player_pokemon.resolve_move(self.player_pokemon, self.enemy_pokemon, move)
        self.enemy_healthbar.update_healthbar(self.enemy_pokemon)
        if self.player_pokemon.has_enemy_fainted(self.enemy_pokemon):
            self.game_state = GameState.WON
        else:
            self.game_state = GameState.ENEMY_TURN
    
    def handle_enemy_turn(self):
        current_time = pygame.time.get_ticks()

        if self.last_attack_time== 0:
            self.last_attack_time = current_time

        if current_time - self.last_attack_time < self.wait_time:
            return

        move = random.randint(0, 3)    
        self.enemy_attack(self.enemy_pokemon.moves[move])
        self.last_attack_time = 0
        

    def enemy_attack(self, move):
        print(f"{self.enemy_pokemon.name} attacked {self.player_pokemon.name}")
        self.enemy_pokemon.resolve_move(self.enemy_pokemon, self.player_pokemon, move)
        self.player_healthbar.update_healthbar(self.player_pokemon)
        if self.enemy_pokemon.has_enemy_fainted(self.player_pokemon):
            self.game_state = GameState.LOST
        else:
            self.game_state = GameState.PLAYER_TURN