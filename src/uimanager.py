from button import Button
from scenes import draw_main_menu, draw_main_menu_text
class UIManager:
    def __init__(self):
        self.game_buttons = None
        self.main_menu_buttons = Button.create_main_menu_buttons()

    def draw_main_menu(self, screen, font):
        draw_main_menu(self.main_menu_buttons)
        draw_main_menu_text(screen, font, (0,0,0), 220, 150)
    
    def is_pokemon_clicked(self):
        return Button.button_clicked(self.main_menu_buttons)
    
    def is_move_clicked(self):
        return Button.move_button_clicked(self.game_buttons[1:])
    
    def create_game_buttons(self, buttons):
        self.game_buttons = Button.create_game_buttons(buttons)
    
    def is_main_menu_button_clicked(self):
        return self.game_buttons[0].check_click()
        

