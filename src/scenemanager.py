from enum import Enum, auto

class Scene(Enum):
    MAIN_MENU = auto()
    BATTLE_SCREEN = auto()
    GAME_OVER = auto()


class SceneManager:
    def __init__(self):
        self.current_scene = Scene.MAIN_MENU
        self.has_player_chosen = False
    
    def go_to(self, scene_name):
        self.current_scene = scene_name