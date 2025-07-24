class SceneManager:
    def __init__(self):
        self.current_scene = "main_menu"
        self.has_player_chosen = False
    
    def go_to(self, scene_name):
        self.current_scene = scene_name