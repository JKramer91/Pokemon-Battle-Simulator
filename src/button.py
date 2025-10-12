import pygame
from constants import *
class Button:
    screen = None
    font = None
    def __init__(self, x, y, text, value = None, width = 150, height = 50,):
        self.x = x
        self.y = y
        self.text = text
        self.value = value if value else text.lower()
        self.rect = pygame.rect.Rect((self.x, self.y), (width, height))
        self.clicked = False
        
        # Caching
        self.text_surface = self.font.render(self.text, True, 'black')
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

        self.normal_surface = pygame.Surface((width, height))
        self.normal_surface.fill('gray')
        pygame.draw.rect(self.normal_surface, 'black', self.normal_surface.get_rect(), 2, 5)

        self.hover_surface = pygame.Surface((width, height))
        self.hover_surface.fill('dark gray')
        pygame.draw.rect(self.hover_surface, 'black', self.hover_surface.get_rect(), 2, 5)

    @classmethod
    def set_screen_and_font(cls, screen, font):
        cls.screen = screen
        cls.font = font

    @classmethod
    def create_game_buttons(cls, moves):
        row_x_start = (1280 - (2 * BUTTON_WIDTH + PADDING_X)) // 2
        row1_y = 765 - BOTTOM_OFFSET - (BUTTON_HEIGHT + PADDING_Y)
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
            cls(565, 420, "Pikachu", "pikachu"),
            cls(565, 480, "Bulbasaur", "bulbasaur"),
            cls(565, 540, "Squirtle", "squirtle"),
            cls(565, 600, "Charmander", "charmander")
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
        surface = self.hover_surface if self.check_click() else self.normal_surface

        self.screen.blit(surface, self.rect.topleft)
        self.screen.blit(self.text_surface, self.text_rect)
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False