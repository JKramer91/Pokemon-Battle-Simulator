import pygame
from constants import *
class Button:
    screen = None
    font = None
    def __init__(self, x, y, text, value = None, width = 150, height = 50):
        self.x = x
        self.y = y
        self.text = text
        self.value = value if value else text.lower()
        self.rect = pygame.rect.Rect((self.x, self.y), (width, height))
        self.clicked = False
    @classmethod
    def set_screen_and_font(cls, screen, font):
        cls.screen = screen
        cls.font = font

    @classmethod
    def create_game_buttons(cls, moves):
        row_x_start = (1280 - (2 * BUTTON_WIDTH + PADDING_X)) // 2
        row1_y = 720 - BOTTOM_OFFSET - (BUTTON_HEIGHT + PADDING_Y)
        row2_y = row1_y + BUTTON_HEIGHT + PADDING_Y
        
        buttons = [
            cls(1100, 30, "Main Menu"),
            cls(row_x_start, row1_y, cls.capitalize(moves[0]["name"])),
            cls(row_x_start + BUTTON_WIDTH + PADDING_X, row1_y, cls.capitalize(moves[1]["name"])),
            cls(row_x_start, row2_y, cls.capitalize(moves[2]["name"])),
            cls(row_x_start + BUTTON_WIDTH + PADDING_X, row2_y, cls.capitalize(moves[3]["name"])),
        ]
        return buttons
    
    @classmethod
    def create_main_menu_buttons(cls):
        buttons = [
            cls(360, 200, "Pikachu", "pikachu"),
            cls(360, 300, "Bulbasaur", "bulbasaur"),
            cls(360, 400, "Squirtle", "squirtle"),
            cls(360, 500, "Charmander", "charmander")
        ]
        return buttons
    
    @staticmethod 
    def capitalize(text):
        arr = text.split("-")
        arr = [v.capitalize() for v in arr]
        return " ".join(arr)

    @staticmethod
    def button_clicked(buttons):
        for button in buttons:
            if button.check_click():
                return True, button.value
        return False, None
    
    @staticmethod
    def move_button_clicked(buttons):
        for i in range(0, 4):
            if buttons[i].check_click():
                return True, i
        return False, None
    
    def draw(self):
        text_surface = self.font.render(self.text, True, 'black')
        
        text_rect = text_surface.get_rect(center=self.rect.center)
        if self.check_click():
            pygame.draw.rect(self.screen, 'dark gray', self.rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, 'gray', self.rect, 0, 5)

        pygame.draw.rect(self.screen, 'black', self.rect, 2, 5)
        self.screen.blit(text_surface, text_rect)
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False